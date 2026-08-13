class Student: 
    def getstudent(self):
        pass

class CE(Student):
    def getstudent(self):
        print("Mrunali Sawant is CE Student")

class IT(Student):
    def getstudent(self):
        print("Mrunali Sawant is IT Student")

class EXTC(Student):
    def getstudent(self):
        print("Mrunali Sawant is EXTC Student")


s = CE()
s.getstudent()