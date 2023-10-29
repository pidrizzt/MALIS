class Module_Person:
    def __init__(self, name, age) : # initialize constructor for the object to assign the object its properties
        self.name = name
        self.age = age
    
    def print_info(self) : # method of the object that can be used
        print('My name is ', self.name,' and I am ',self.age)

class Module_Student(Module_Person) :
    def __init__(self, name, age, graduation_year=None) :
        super().__init__(name, age)
        self.gradY = graduation_year
        
    def print_graduation(self, description) :
        print(self.name, ' is a class ',self.gradY,' student. ',description)