class Phone:

    def call(self):
        print("call me phone")


class Samsumg(Phone):
    def call(self):
        #pass
       super().call()
       print("call me samsung")


s = Samsumg()
s.call()




