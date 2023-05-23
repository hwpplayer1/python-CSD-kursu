def get_odd_even(iterable):
    odd = []
    even = []
    for x in iterable:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return odd, even

odd, even = get_odd_even([1, 2, 3, 4, 5])
print(odd, even)
