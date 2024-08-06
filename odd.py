range(1,10)
count=0
for i in range(1,10):
    if i%2!=0:
        count=count+1
        print(i)
        i=i+1
    else:
        i=i+1
print("We have " +str(count)+ " odd numbers" )

#Using formatted string
count=0
for i in range(1,10):
    if i%2!=0:
        count=count+1
        print(i)
        i=i+1
    else:
        i=i+1
print(f"We have {count} odd numbers" ) #Using formatted string
