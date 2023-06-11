numbers = [12, 1221, 13431, 12345, 197262]
a = [number for number in numbers if str(number) == str(number)[::-1]]
print(a)
