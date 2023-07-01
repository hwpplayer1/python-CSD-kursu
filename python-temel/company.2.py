class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def disp(self):
        print('Adı Soyadı: {}'.format(self.name))
        print('Adres: {}'.format(self.address))

class Worker(Employee):
    def __init__(self, name, address, shift):
        super(Worker, self).__init__(name, address)  # Employee.__init_(self, name, address)
        self.shift = shift

    def disp(self):
        super(Worker, self).disp()           # Employee,disp(self)
        print('Vardiya: {}'.format(self.shift))

class Manager(Employee):
    def __init__(self, name, address, department):
        super(Manager, self).__init__(name, address)    # Employee.__init__(self, name, address)
        self.department = department

    def disp(self):
        super(Manager, self).disp()           # Employee,disp(self)
        self.department = department
    def disp(self):
        super(Manager, self).disp()           # Employee.disp(self)
        print('Departman: {}'.format(self.department))

class Executive(Manager):
    def __init__(self, name, address, department, region):
        super(Executive, self).__init__(name, address, department) # Manager.__init__(self, name, address, department)
        self.region = region

    def disp(self):
        super(Executive, self).disp()        # Manager.disp(self).
        print('Bölge: {}'.format(self.region))

e = Executive('Salih Bulut', 'Kazlıçeşme', 'Üretim', "Ortadoğu")
e.disp()
