num = int(input("Enter number: "))
x = num
rev = 0

while x > 0:
    rem = x % 10
    rev = rev*10+rem
    x = x // 10
def isPrime(n):
    if(n==0 or n==1):
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def checktwistedprime(n):
    if(isPrime(n)== False):
        return False
    else:
        return isPrime(rev)



print(f"Reversed number :{rev}")

if (isPrime(num) and isPrime(rev)):
    print(num," is Twisted Prime")
else:
    print(num," is not Twisted Prime")



i = 2
for i in range(2,200):
    if checktwistedprime(i)== True:
        print(i,end=" ")
    i = i + 1



