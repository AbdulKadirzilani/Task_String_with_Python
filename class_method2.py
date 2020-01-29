class Student:
    roll=""
    gpa =""
    def setvalue(self,roll,gpa):
        self.roll= roll
        self.gpa= gpa


    def display(self):
        return (f"Roll:{self.roll}, Gpa:{self.gpa}")

rahim = Student()
rahim.setvalue(101,3.5)
print(rahim.display())

rana = Student()
rana.setvalue(102,3.6)
print(rana.display())

