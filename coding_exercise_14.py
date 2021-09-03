numbers = input("Please enter three numbers: ")

strings = numbers.split(",")

pole = []

for item in strings:
    pole.append(int(item))

x, y, z = pole

result = x + y - z
   
print(result)

