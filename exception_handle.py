def add(x,y):
    try:
        return x/y

    except Exception as e:
        return ("zero division error by",e)


print(add (4,0))