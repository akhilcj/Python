numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)
print(len(numbers))
numbers.insert(0, -1)
print(numbers)

numbers.remove(3)
print(numbers)
print(1 in numbers)
print(10 in numbers)
numbers.clear()
print(numbers)