country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]
mayor= ["柯文哲","朱立倫","鄭文燦","林佳龍","賴清德","陳菊"]

dic = {country: mayor for country, mayor in zip(country, mayor)}

with open("CM.txt", "a") as f:
    for c, m in dic.items():
        f.write(str(c) + ":" + str(m) + "\n")