import anna

a = int(input("a: "))
b = int(input("b: "))
o = input("act:  ")

if o == "+":
      print (f"{a} + {b} = {anna.add(a,b)}")
elif o == "-":
      print (f"{a} -{b} = {anna.diff(a,b)}")
elif o == "/":
      print (f"{a}  / {b} = {anna.div(a,b)}")
elif o == "*":
     print (f"{a}  * {b} = {anna.mul(a,b)}")
else:
    print("неправильна дія")