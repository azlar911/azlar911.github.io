import p128_2_class

t = p128_2_class.traffic("T1", 0)
t.hello()
print()

c = p128_2_class.car("Car1", 5, 100)
print(c.__str__())
c.drive()
print(c.getCount())

c1 = p128_2_class.car("Car2", 7, 80)
print(c1.__str__())
c1.drive()
print(c1.getCount())

b = p128_2_class.boat("Boat1", 70, 100)
print(b.__str__())
b.sail()
print(b.getCount())

p = p128_2_class.plane("Plane1", 200, 1000)
print(p.__str__())
p.fly()
print(p.getCount())