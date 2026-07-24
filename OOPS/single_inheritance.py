# Example of single inheritance in Python

class College: 
    def getCollege(self, clgname, location):
        self.clgname = clgname
        self.location = location

    def putCollege(self):
        print("College Name:", self.clgname)
        print("Location:", self.location)


class Student(College):
    def getStudent(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept

    def putStudent(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.dept)


s = Student()
s.getCollege("Usha Mittal Institute of Technology", "Mumbai")
s.getStudent(1, "Mrunali Sawant", "Computer Engineering")
s.putCollege()
s.putStudent()
        