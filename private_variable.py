class stu:
    total=0
    def __init__(self):
        self.__attri="it is hidden"
        type(self).total+=1
t=stu()
print(stu.total)
# print(t.__attri)    # this gives error as the private varible is name mangled by python and __total is now _stu__total
print(t._stu__attri)