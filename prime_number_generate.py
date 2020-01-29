# If num is divisible by any number
# between 2 and val, it is not prime

start = 11
end = 33

for val in range(start, end + 1):

    if val > 1:
        for n in range(2, val//2):
            if (val % n) == 0:
                #print(val)
                #print(val, "is not a prime number")
                break
        else:
            print(val)