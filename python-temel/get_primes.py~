def get_primes(count):
    def isprime(val):
        if val % 2 == 0:
            return val == 2
        for i in range(3, int(val ** 0.5) + 1, 2):
            if val % i == 0:
                return False
            return True

    i = 2
    while count > 0:
        if isprime(i):
            count -= 1
            yield i
        i += 1
    
