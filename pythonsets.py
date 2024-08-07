numbers = [1,1,2,3,4]

first = set(numbers) #set(numbers) gives unique values in numbers
second = {1,5}
print(numbers)
print(first)
print(first | second) #union of sets
print(first & second) #intersection of sets
print(first - second) #difference of sets
print(first ^ second) #symmetric difference
#print(first[0]) will result in error as set doesn't support indexing
if 1 in first:
    print("Yes")