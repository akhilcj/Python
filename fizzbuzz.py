def fizz_buzz(input):
    if input % 3 == 0 and input % 5 !=0:
        message = "Fizz"
        print(message)
    elif input % 5 == 0 and input % 3 !=0:
        message = "Buzz"
        print(message)
    elif input % 3== 0 and input % 5==0:
        message = "FizzBuzz"
        print(message)
    else:
        print(input)
    return " "

print(fizz_buzz(15))