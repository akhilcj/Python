def lcm(a, b):
    greatest = max(a,b)
    smallest = min(a,b)
    for i in range(greatest, (a*b+1), greatest):
        if i % smallest == 0:
            return i


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
LCM = int(lcm(num1, num2))
print(f"The LCM of {num1} and {num2} is {LCM}")