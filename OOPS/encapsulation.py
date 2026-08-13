class Student: 
    def __init__(self, name, branch):
        self.name = name
        self.__branch = branch  # Private attribute

    def get_branch(self):
        return self.__branch  # Public method to access the private attribute

s = Student("Mrunali", "Computer Science")
print(s.get_branch())  # Accessing the private attribute through a public method
print(s.__branch)  # This will raise an AttributeError since __branch is private
