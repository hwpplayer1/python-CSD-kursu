class Student:
    x = 10                           # sınıf özniteliği, sınıfın bir elemanı, nesnenin değil
    print(x)                         # sınıf özniteliği olan x kullanılıyor

    def __init__(self, name, no):
        self.name = name
        self.no = no

    def disp(self):
        print("İsim = {}, No = {}".format(self.name, self.no))
        print("x = {}".format(Student.x))      # x değil, Student.x

s = Student("Ali Serçe", 123)
s.disp()
print("x = {}".format(Student.x))              # x değil, Student.x
