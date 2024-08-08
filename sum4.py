def add_numbers_recursive(x,y):
    if y == 0:
        return x
    else:
        return add_numbers_recursive(x+1,y-1)


num1=float(input("Enter number1: "))
num2=float(input("Enter number2: "))
sum = add_numbers_recursive(num1,num2)

print(f"The sum of {num1} and {num2} is {sum}")