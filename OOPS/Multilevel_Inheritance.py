# Example of Multilevel inheritance in Python

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

class Exam(Student):
    def getExam(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2

    def putExam(self):
        print("Subject 1:", self.sub1)
        print("Subject 2:", self.sub2)


e = Exam()
e.getCollege("Usha Mittal Institute of Technology", "Mumbai")
e.getStudent(1, "Mrunali Sawant", "Computer Engineering")   
e.getExam("Python", "Java")
e.putCollege()
e.putStudent()
e.putExam()