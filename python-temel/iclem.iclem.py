a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[y for y in x if y % 2 == 0] for x in a]
print(b)
