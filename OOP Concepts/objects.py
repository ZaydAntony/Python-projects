
# in this folder we learn all about objects in python

class Student: # This is a class/ object called student
    year_of_study = 2025 # class variable
    def  __init__(self,name,age,course): # This is a constructor
        self.name =name;
        self.age = age; # instance variable
        self.course = course

    def register(self): # A method.
        print(f"{self.name} registered for the special exams");
        print(f"The student is {self.age} yrs old");
        print(f"The student is taking {self.course}");


student1 =Student("Antony", 22, "Data Science");

print(student1.register());

print(student1.year_of_study)
        