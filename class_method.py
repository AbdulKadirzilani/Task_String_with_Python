class Student:
    roll=" "
    gpa =" "

    def display(self):
        return (f"Roll:{self.roll}, Gpa:{self.gpa}")

rahim = Student()
rahim.roll = 101
rahim.gpa = 3.5
print(rahim.display())

rana = Student()
rana.roll = 102
rana.gpa = 3.6
print(rana.display())

