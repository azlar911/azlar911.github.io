with open("news.txt", "r") as f:
    content = f.read()

a = ""
for c in content:
    if not c.isalnum():
        a += c

with open("news.txt", "w") as f:
    f.write(a)
