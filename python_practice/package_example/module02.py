class Animal:
    __x = 0
    def __init__(self, name):
        self.name = name
        Animal.__x += 1
    def run(self):
        print(self.name, 'runs')
    def jump(self):
        print(self.name, 'jumps')
    @classmethod
    def getX(cls):
        return(cls.__x)

class Cat(Animal):
    def shout(self):
        print(self.name, 'Meow')

class Dog(Animal):
    def shout(self):
        print(self.name, 'Bark')

class Human(Animal):
    # override the method from superclass
    # the __init__() of Animal isn't triggered
    # therefore the value of ponshane.__x won't increase
    def __init__(self, name):
        self.name = name + "博士"
    # override the method from superclass
    def run(self):
        print(self.name, '跑不動')
    def shout(self):
        print(self.name, '大叫醒醒吧肥宅 你沒有妹妹')

class Rostin(Animal):
    # override the method from superclass
    # use super() to trigger the __init__ of Animal
    # therefore the value of ponshane.__x will increase
    def __init__(self, name):
        self.name = "廢物" + name
        super().__init__("廢物" + name)
    # override the method from superclass
    def run(self):
        print(self.name, '也是跑不動')
    def shout(self):
        print(self.name, '大叫等下要去看自殺突擊隊囉')
        
if __name__ == "__main__":
    lucky = Dog("Lucky")
    lucky.run()
    lucky.jump()
    lucky.shout()
    print("lucky.__x = {0}".format(lucky.getX()))
    mimi = Cat("Mimi")
    mimi.run()
    mimi.jump()
    mimi.shout()
    print("mimi.__x = {0}".format(mimi.getX()))
    ponshane = Human("Ponshane")
    ponshane.run()
    ponshane.jump()
    ponshane.shout()
    print("ponshane.__x = {0}".format(ponshane.getX()))
    rostin = Rostin("rostin")
    rostin.run()
    rostin.jump()
    rostin.shout()
    print("rostin.__x = {0}".format(rostin.getX()))