def floorsqrt(x):
    if (x==0 or x==1):
        return x


    i=1
    result = 1
    while (result<=x):
        i+=1
        result = i*i
    return i - 1


#x=25
#print(floorsqrt(x))

m = int(input("Enter number:"))
res = floorsqrt(m)
print(f"The squareroot is {res}")