class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def disp_employee(self):
        print('Adı Soyadı: {}, Adres: {}'.format(self.name, self.address))

class Worker(Employee):
    def __init__(self, name, address, shift):
        super(Worker, self).__init__(name, address)  # Employee,__init__(self, name, address)
        self.shift = shift

    def disp_worker(self):
        print('Adı Soyadı: {}, Adres: {}, Vardiya: {}'.format(self.name, self.address,
self.shift))


e = Worker('Ali Serçe', 'Maslak', 'Sabah')
e.disp_worker()
