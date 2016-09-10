from flask import Flask, abort, jsonify, request
from passlib.apps import custom_app_context as pwd_context
from flask_httpauth import HTTPBasicAuth
import sqlite3 as sql

app = Flask(__name__)
auth = HTTPBasicAuth()

def hash_password(password):
    password_hash = pwd_context.encrypt(password)
    return password_hash

def verify_hash(password, password_hash):
    return pwd_context.verify(password, password_hash)

@auth.verify_password
def verify_password(username, password):
    
    con = sql.connect('database.db')
    cur = con.cursor()    
    cur.execute("SELECT * FROM Users WHERE username =(?)", (username, ))
    row = cur.fetchone()
    if row:
	    return verify_hash(password, row[1])
    else:
	    return False

@app.route('/users', methods=['POST'])
def reg():
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Users (username, password) VALUES (?,?)", (request.json['username'], hash_password(request.json['password']) ,))
    conn.commit()
    return jsonify({'Message': 'Register successfully'}), 201

@app.route('/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute("select * from Tasks")
    rows = cur.fetchall()
    task_list = list()
    for row in rows:
        each_task = dict()
        each_task['Uri'] = row[0]
        each_task['Title'] = row[1]
        each_task['Description'] = row[2]
        each_task['Done'] = row[3]
        task_list.append(each_task)
    conn.close()
    return jsonify(task_list)

@app.route('/tasks', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or not 'Uri' in request.json:
        abort(400)
    conn = sql.connect('database.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO Tasks (Uri,Title,Description,Done) VALUES (?,?,?,?)"
        , (request.json['Uri'], request.json['Title'], request.json.get('Description', ''), 0))
        conn.commit()
    return jsonify({'Message': 'Insert successfully'}), 201

@app.route('/tasks/<task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    conn = sql.connect('database.db')
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM Tasks WHERE Uri=(?)", (task_id,))
        msg = "delete sucessfully!"
        conn.commit()
    except:
        msg = "Something worong!"
    finally:
        conn.close()
        return jsonify({'Message': msg})

@app.route('/tasks/<task_id>', methods=['PUT'])
@auth.login_required
def update_task(task_id):
    conn = sql.connect('database.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Tasks WHERE Uri = (?)", (task_id,))
        row = cur.fetchone()
        each_task = dict()
        each_task['Title'] = request.json.get('Title', row[1])
        each_task['Description'] = request.json.get('Description', row[2])

        cur.execute("UPDATE Tasks SET Title = (?), Description = (?) WHERE Uri = (?)", (each_task['Title'], each_task['Description'],task_id,))
        conn.commit()
    return jsonify({'Message': 'Update successfully'})
    # You need to update Title and Description column.
    # Then, return your response and correct response code to your client!

@app.route('/tasks/<task_id>', methods=['GET'])
@auth.login_required
def get_a_task(task_id):
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute("select * from Tasks WHERE Uri = (?)", (task_id,))
    row = cur.fetchone()
    each_task = dict()
    each_task['Uri'] = row[0]
    each_task['Title'] = row[1]
    each_task['Description'] = row[2]
    each_task['Done'] = row[3]
    return jsonify(each_task)

if __name__ == '__main__':
    app.run(debug=True)
