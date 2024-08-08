def pushzeroestoend(arr,n):
    count = 0
    for i in range(n):
        if arr[i]!= 0:
            arr[count] = arr[i]
            count+=1


    while count < n:
        arr[count]=0
        count+=1

#arrays=[1,2,3,5,0,8,0,9,0,88]
#n= len(arrays)
arrays = []
size= int(input("Enter array size: "))
for i in range(size):
    num = int(input(f"Enter array element {i+1}: "))
    arrays.append(num)
    i+=1
print(arrays)
n = len(arrays)
pushzeroestoend(arrays, n)
print(arrays)

