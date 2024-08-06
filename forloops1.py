successfull = True
for i in range(3):
    print("Attempt")
    if successfull:
        print("Successfull")
        break

successfull = False
for i in range(3):
    print("Attempt")
    if successfull:
        print("Successfull")
        break
else:
    print("Attempted 3 times and failed ")

successfull = True
for i in range(3):
    print("Attempt")
    if successfull:
        print("Successfull")
        break
else:
    print("Attempted 3 times and failed ")