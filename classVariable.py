class Car:
    whools = 5
    def __init__(self):

        self.mil = 10
        self.com ="mbw"
        #self.mil = 12

c1 = Car()
c2 = Car()
Car.whools = "pjero"

#Car.mil = 12

print(c1.mil , c1.com ,c1.whools )
print(c2.mil , c2.com,c2.whools )