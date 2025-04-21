class stu:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def makeObj(cls,sequence):
        # print(*sequence)
        return stu(*sequence)
    def addage(self,num):
        if isinstance(num,str):
            raise ValueError("Expected positive value")
        else:
            self.age+=num

l=stu.makeObj(["name",2])
s1=stu("A",6)
# s1.addage("-5")
print(l.name,l.age)