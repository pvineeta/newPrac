'''
wirte a class which have 2 methods where 1 takes 2 arguments & return sum of those &
the other one check whether given agruments are int or not, if not int,
convert them into int &return the value.
'''

class Super:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b


    def sum(self, a, b):
        self.a, self.b = a, b
        result = self.check()
        if result:
             print(self.a + self.b)

    def check(self):
        try:
            self.a = int(self.a)
            self.b = int(self.b)
            return True
        except:
             print("Entered values are not acceptable")


x = Super()
y = x.sum(3, '2')
