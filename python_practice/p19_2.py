data = list()
new = {"name": "a", "id":"b03", "grade": {"math":9, "chin":8, "eng":7}}
data.append(new)
new["name"] = "b"
new["id"] = "b04"
new["grade"]["math"] = 1
new["grade"]["chin"] = 1
new["grade"]["eng"] = 1
data.append(new)
new["name"] = "c"
new["id"] = "b05"
new["grade"]["math"] = 1
new["grade"]["chin"] = 2
new["grade"]["eng"] = 3
data.append(new)
new["name"] = "d"
new["id"] = "b06"
new["grade"]["math"] = 3
new["grade"]["chin"] = 2
new["grade"]["eng"] = 1
data.append(new)
new["name"] = "e"
new["id"] = "b02"
new["grade"]["math"] = 10
new["grade"]["chin"] = 10
new["grade"]["eng"] = 10
data.append(new)



print(data)