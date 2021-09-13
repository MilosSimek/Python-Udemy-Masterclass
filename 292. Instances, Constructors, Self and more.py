class Kattle:

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False        

    def switch_on(self):
        self.on = True


kenwood = Kattle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kattle("Hamilton", 14.55)

print(f"Models: {kenwood.make} = {kenwood.price}, {hamilton.make} = {hamilton.price}")

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kattle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)


