# Class and Object in Python

class Student: 
    def __init__(self, id, name, dept):  
        self.id = id
        self.name = name
        self.dept = dept

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)  
        print("Department:", self.dept)

s = Student(1, "Mrunali Sawant", "Computer Engineering")
s.display()