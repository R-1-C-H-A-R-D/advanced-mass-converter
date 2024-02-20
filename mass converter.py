mass = int (input("What is your mass: "))
unit = input("lbs(l) or kgs(kg)")
if unit.lower() == "l":
    converted = mass * 0.45
    print (f"You are {converted} kgs")
else:
    converted = mass / 0.45
    print (f"you are {converted} lbs")
#end