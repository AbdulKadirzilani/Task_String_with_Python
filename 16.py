
def check(number):
    if number%2==0:
        c= "EVEN"
        return c
    else:
        c ="ODD"
        return c


number = int(input())
print(check(number))