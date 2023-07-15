class Employee:
    def __init__(self, name):
        self.name = name

class Worker(Employee):
    def __init__(self, name, weekHours):
        super().__init__(name)
        self.weekHours = weekHours

    def calc_salary(self):
        return self.weekHours * 30

class Manager(Employee):
    def __init__(self, name, prim):
        super().__init__(name)
        self.prim = prim

    def calc_salary(self):
        return 7000 + 7000 * self.prim

class SalesPerson(Employee):
    def __init__(self, name, prim):
        super().__init__(name)
        self.prim = prim

    def calc_salary(self):
        return 3000 + 3000 * self.prim

employees = [Worker('Ali', 40), Manager('Veli', 0.20), SalesPerson('Selami', 0.10)]

for emp in employees:
    print('Adı: {}, Maaş: {}'.format(emp.name, emp.calc_salary()))

salary = 0
for emp in employees:
    salary += emp.calc_salary()

print('Toplam Maaş: {}'.format(salary))
