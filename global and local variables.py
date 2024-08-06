message = "a"

#def greet(name):
    #message = "b"

#greet(Mosh)
#print(message)

#message = "a"

def greet(name):
    global message  #here the global variable a is updated to b
    message = "b"

greet("Mosh")
print(message)