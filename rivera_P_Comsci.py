sum = 0
difference = 0
qnum = float(input("Enter a number"))
wnum = float(input("Enter another number"))

def calculate_sum():
    global sum
    sum = qnum + wnum
    print(sum)
def calculate_difference():
    global difference
    difference = qnum - wnum
    print(difference)
calculate_sum()
calculate_difference()