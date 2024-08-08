def missingnumber(arr,n):
    sum_arr=sum(arr)
    expected_sum =(n*(n+1))//2

    return expected_sum - sum_arr


#arr = [1,2,3,5]
#n=5
#print(missingnumber(arr,n))
my_list = []
i=0
size = int(input("Enter array size: "))
#print(len(my_list))
while i <= size:
    for i in range(i,size):
        numbers = int(input("Enter array elements: "))
        i = i + 1
        my_list.append(numbers)
        i += 1

intseq=int(input("Enter size of intended seq: "))
missing=missingnumber(my_list,intseq)
print(my_list)
print(f"The missing element is {missing}")


