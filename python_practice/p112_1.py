import p112_class

acc = p112_class.Bank("azlar", [20,30])
print(acc.accountTotal())
acc.addProperty(90)
print(acc.accountTotal())
acc.addProperty(80)
print(acc.accountTotal())

print(acc.__str__())