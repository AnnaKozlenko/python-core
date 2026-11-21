def  add (a, b) :
    return a + b

def diff(a,b ):
    return a - b

def div(a,b):
    if b == 0:
        return "не можна ділити на нуль"
    else:
        return a / b

def mul(a,b):
    return a * b

a = int(input("a: "))
b = int(input("b: "))
o = input("act:  ")

if o == "+":
      print (f"{a} + {b} = {add(a,b)}")
elif o == "-":
      print (f"{a} -{b} = {diff(a,b)}")
elif o == "/":
      print (f"{a}  / {b} = {div(a,b)}")
elif o == "*":
     print (f"{a}  * {b} = {mul(a,b)}")
else:
    print("неправильна дія")