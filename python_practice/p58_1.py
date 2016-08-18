country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]
mayor= ["柯文哲","朱立倫","鄭文燦","林佳龍","賴清德","陳菊"]

dic = {coun:may for coun, may in zip(country, mayor)}

print(dic)