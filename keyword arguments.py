def increment(number,by=1): #Here number is req parameter and by is optional parameter
    return number + by #By default by=1

#result = increment(2,1)
#print(result)


#result = increment(2,by=1) #Here by is the keyword argument
#print(result)

result = increment(2)
print(result)

result = increment(5,7)
print(result)