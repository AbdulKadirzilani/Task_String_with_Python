
def smart_sum(num1,num2,num3):
    if (num1 ==num2):
        sum = num1+ num3
        return sum
    elif (num1 == num3):
        sum = num1 + num2
        return sum
    elif (num2 ==num3):
        sum = num1+ num2
        return sum
    else:
        sum = num1+num2+num3
        return sum

print("Enter three value")
num1= int(input())

num2= int(input())
num3 = int(input())
print(smart_sum(num1,num2,num3))

