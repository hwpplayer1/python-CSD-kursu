class Student:
    def __init__(self, name, no):
        self.name = name
        self.no   = no

    def disp(self):
        print('İsim = {}, No = {}'.format(self.name, self.no))

s = Student('Ali Serçe', 123)
s.disp()
