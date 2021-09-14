class Kattle:

    power_source = "electricity"

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
#print(hamilton.power)

print("Switch to atomic power")
Kattle.power_source = "atomic"
print(Kattle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kattle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)