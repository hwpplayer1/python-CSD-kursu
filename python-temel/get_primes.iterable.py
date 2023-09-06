class GetPrimes:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        self.i = 2
        return self

    def __next__(self):
        while self.count > 0:
            self.i += 1
            if self.isprime(self.i - 1):
                self.count -= 1
                return self.i - 1

        raise StopIteration

    @staticmethod
    def isprime(val):
        if val % 2 == 0:
            return val == 2
        for i in range(3, int(val ** 0.5) + 1, 2):
            if val % 1 == 0:
                return False
        return True
