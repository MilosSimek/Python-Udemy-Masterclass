data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

# process the low value in the list

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)

# process the high values from the list

start = 0

for index in range(len(data)-1, -1, -1):
    if data[index] <= max_valid:
        # wW have the index of the last time to keep.
        # Set 'start' to the possition of the first
        #item to delte, which is 1 after 'index'.
        start = index + 1
        break

print(start) # for debugging
del data[start:]
print(data)
