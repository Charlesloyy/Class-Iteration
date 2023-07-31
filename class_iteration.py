class MyNumber:
    def __iter__(self):
        self.a = 1
        self.x = 0
        return self
    def __next__ (self):
        
        self.z = self.a + self.x
        self.x = self.a
        self.a = self.z
        return self.x


myclass = MyNumber()
myiter = iter(myclass)
##print(next(myiter))
##print(next(myiter))
##print(next(myiter))
##print(next(myiter))
##print(next(myiter))
##print(next(myiter))

fiban = []
for _ in range(50):
    fiban.append(next(myiter))
print(fiban)
