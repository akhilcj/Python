def save_user(**user):
    print(user)

save_user(id=1,name="John",age=22) #dictionary will be printed

def save_user(**user):
    print(user["name"])

save_user(id=1,name="John",age=22)

def save_user(**user):
    print(user["age"])

save_user(id=1,name="John",age=22)