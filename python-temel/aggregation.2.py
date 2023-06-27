class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def disp(self):
        print(f'{self.name}, {self.specialty}')

class Hospital:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def disp(self):
        for doctor in self.doctors:
            doctor.disp()

hospital = Hospital()

doctor1 = Doctor('Ali Serçe', 'İç Hastalıkları')
doctor2 = Doctor('Medeni Demir', 'Psikiyatri')

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

hospital.disp()
