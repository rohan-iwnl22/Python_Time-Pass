print("!! Welcome To Tip Calculator !!")
bill = float(input("What was the total bill?$"))
tip = int(input("What percentage tip you would like to give? 10,12 or 15?"))
new_bill = bill+(bill*tip/100)
person = int(input("How many persons you wanna split the bill into?"))
split = (new_bill/person)
split = round(split,2)
print(f"Each person should pay ${split}")
