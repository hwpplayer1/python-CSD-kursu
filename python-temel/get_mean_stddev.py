import math

def get_mean_stddev(iterable):
    total = 0
    count = 0
    for x in iterable:
        total += x
        count += 1
    mean = total / count

    total = 0
    for x in iterable:
        total += (x - mean) ** 2
    stddev = math.sqrt(total / count)

    return mean, stddev

mean, stddev = get_mean_stddev([1, 2, 5, 6, 8])
print(mean, stddev)
