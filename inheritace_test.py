class Phone:

    def call(self):
        print("Call me now")
    def message(self):

        print("message me")


class Samsung(Phone):

    def call2(self):
        print("Call me now by samsung")

    def message2(self):
        print("message me by samsung")
    def music(self):
        print("Show music")

p = Phone()
p.call()
p.message()

s = Samsung()
s.call2()
s.call()

print(issubclass(Samsung,Phone))

print(issubclass(Phone,Samsung))