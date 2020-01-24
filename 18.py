
def drivering(speed):
    if speed <=60:
        c = "the result is 0"
        return c

    elif speed >=60 and speed<=80:
        c = "the result is 1"
        return c

    elif speed >=81:
        c = "the result is 2"
        return c

print("ENTER THE SPEED\n")
speed  = int(input())
print(drivering(speed))