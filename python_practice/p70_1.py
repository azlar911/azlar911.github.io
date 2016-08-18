country = ["台北市","新北市","桃園市","台中市","台南市","高雄市"]

with open("country.txt", "w") as f:
	for i in country:
		f.write(i + "\n")
		