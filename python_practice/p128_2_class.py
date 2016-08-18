class traffic:
    total = 0
    def __init__(self, name, capacity):
        traffic.total += 1
        self.name = name
        self.capacity = capacity

    @staticmethod
    def hello():
        print("Hello! There is {0} traffic objects created".format(traffic.total))

    @classmethod
    def add(cls, c, n):
        traffic.total += 1
        print("Traffic object No: {0} created".format(traffic.total))
        print("It's a {0}, no:{1}".format(n, c))

class car(traffic):
    __count = 0
    def __init__(self, name, capacity, maxspeed):
        car.__count += 1
        super().add(car.__count, "CAR")
        self.name = name
        self.capacity = capacity
        self.maxspeed = maxspeed
    
    def __str__(self):
        return "Car: {0} can take {1} peoples, maxspeed: {2}\nThere are {3} cars created".format(self.name, self.capacity, self.maxspeed, car.__count)

    def drive(self):
        print("Driving")

    def getCount(self):
        return car.__count

class boat(traffic):
    __count = 0
    def __init__(self, name, capacity, maxspeed):
        boat.__count += 1
        super().add(boat.__count, "BOAT")
        self.name = name
        self.capacity = capacity
        self.maxspeed = maxspeed
    
    def __str__(self):
        return "Boat: {0} can take {1} peoples, maxspeed: {2}\nThere are {3} boats created".format(self.name, self.capacity, self.maxspeed, boat.__count)

    def sail(self):
        print("Sailing")

    def getCount(self):
        return boat.__count

class plane(traffic):
    __count = 0
    def __init__(self, name, capacity, maxspeed):
        plane.__count += 1
        super().add(plane.__count, "PLANE")
        self.name = name
        self.capacity = capacity
        self.maxspeed = maxspeed
    
    def __str__(self):
        return "Plane: {0} can take {1} peoples, maxspeed: {2}\nThere are {3} planes created".format(self.name, self.capacity, self.maxspeed, plane.__count)

    def fly(self):
        print("Flying")

    def getCount(self):
        return plane.__count

if __name__ == "__main__":
    print("Error: This is a module!")