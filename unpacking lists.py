numbers = [1,2,3,4,4,4,4,4,4]

first,second, *other = numbers

print(first)
print(second)
print(other)

num = [1,2,3,4,4,4,4,4,4,9]
first,*others,last = num
print(first)
print(last)
print(others)