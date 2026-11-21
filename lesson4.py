import random

score = 0

while True:
    a = random.randint(2,9)
    b = random.randint(2,9)

    if int(input(f"{a} x {b} = "))== a * b:
        score += 1

    print (f"💎 {score}")
