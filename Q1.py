class calculator:
    def multiply(self,n1,n2=1,n3=1):
        s=n1*n2*n3
        return s
obj=calculator()
print(obj.multiply(2))
print(obj.multiply(3,4))
print(obj.multiply(2,3,4))