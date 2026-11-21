def  add (a, b) :
    return a + b

def diff(a,b ):
    return a - b

a = int(input("a: "))
b = int(input("b: "))


print (f"{a} + {b} = {add(a,b)}")
print (f"{a} -{b} = {diff(a,b)}")