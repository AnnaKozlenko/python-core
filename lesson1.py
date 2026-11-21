name  = input ("What your name? ")
print (f"Hello, {name}")
age =  int(input("how old are you?"))
print(f"you are {age} years old")

if age < 13:
    print("you are child")
elif age < 18:
    print("you are teenager")
else:
    print("you are adult")