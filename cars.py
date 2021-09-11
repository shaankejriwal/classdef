class Cars(object):
    def __init__(self, model ,colour ,company ,speedlimit ,power):
        self.model = model
        self.colour = colour
        self.company = company
        self.speedlimit = speedlimit
        self.power = power

    def start(self):
        print("the car has been started")

    def stop(self):
        print("the car has stopped moving")

    def accelerate(self):
        print("the car is accelerating")

    def change_gear(self,gear_type):
        print("the car just changed gear")

audi = Cars("Q8","red","audi","280km/h","2500CC")
print(audi.colour)
print(audi.company)
audi.start()

class Fruits(object):
    def __init__(self,name,colour,price):
        self.name = name
        self.colour = colour
        self.price = price

    def available(Self):
        print("the fruit is still available")

    def soldout(self):
        print("the " + self.name + " is sold out")

apple = Fruits("apple","red","150 rs/kg")
print(apple.colour)
apple.soldout()