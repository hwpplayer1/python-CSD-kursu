l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = [val for index, val in enumerate(l) if index % 2 == 0]
print(result)
