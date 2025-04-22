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
    @staticmethod
    def printName(name):
        print(name)
    def __repr__(self):
        return f"{self.name}: {self.age} "
l=stu.makeObj(["name",2])
s1=stu("A",6)
# s1.addage("-5")
attri={"Interest":"Data Science", "College":"JSS"}
for key,value in attri.items():
    setattr(s1,key,value)
print(s1.Interest)
print(l.name,l.age)
s1.printName("name")