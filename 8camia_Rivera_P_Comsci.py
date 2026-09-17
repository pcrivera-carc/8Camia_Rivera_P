
#payment checker
payment = ("Gcash", "Card", "card")
payment = input("Enter your payment method ")

if payment == "Gcash" or payment == "card" or payment == "cash":
    print("valid payment")
else:
    print("invalid payment")





#Grade checker
grade = float(input("Enter your grade "))
if grade >= 101 or grade <= -1:
    print("Invalid, Grade must be between 1 and 100")
else: print("Valid Grade")



#id checker
id = ("2026-1234")
id = input("Enter your id school year ")
if id == "2026-1234":
    print("Valid school year")
else: print("Invalid school year")



#Pin validator
pin = float(input("Enter your pin "))
if pin <= 999 or pin >= 10000:
    print("Invalid pin, please enter 6 digits ")
else: print("Valid Pin")

#student score validator
examscore = float(input("Enter your exam score "))
if examscore <= 100 and examscore >= 0:
     print("valid exam score")
else: print("Invalid exam score, please enter a number between 0 and 100")