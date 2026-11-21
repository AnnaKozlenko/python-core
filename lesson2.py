a = int(input("a: "))
b = int(input("b: "))

o = input("act: ")

if o == "+":
    print(f"{a} + {b} = {a + b}")
elif o == "-":
    print(f"{a} - {b} = {a - b}")
elif o == "*":
    print(f"{a} * {b} = {a * b}")
elif o == "/":
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("на нуль ділити не можна")
else:
    print("Невідома дія")



