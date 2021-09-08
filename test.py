def sum_eo(n, t):
    number = 0
    if t == 'e':
        for i in range(2, n, 2):
            number +=i
        return number
    if t == 'o':
        for i in range(1, n, 2):
            number +=i
        return number
    else:
        return -1

suma = sum_eo(7, 'o')
print(suma)