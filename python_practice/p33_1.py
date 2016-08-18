a = float(input("Height: (m)"))
b = float(input("Weight: (kg)"))
bmi = b / a / a

print("BMI = {0}".format(bmi))

if bmi < 18.5:
	print("過輕")
elif bmi < 24:
	print("適中")
else:
	print("過重")