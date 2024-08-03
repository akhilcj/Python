weight = float(input("Weight : "))

w = str(input("(K)g or (L)bs : "))

if w == "K" or w == "k":
    lbs = float(weight / 0.45)
    print("Weight in Lb: "+str(lbs))
elif w == "L" or w =="l":
    kgs = float(weight * 0.45)
    print("Weight in Kg: "+str(kgs))
else:
    print("Error")
