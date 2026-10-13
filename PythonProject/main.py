from zlib import adler32


def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")
display_header()


name = (input("Enter student name "))
as1 = float(input("Enter assessment 1 "))
as2 = float(input("Enter assessment 2 "))
as3 = float(input("Enter assessment 3 "))
f = (as1 + as2 + as3)/3
display_header()
def display_report():
  print(name)
  if f > 90:
      print("OUTSTANDING")
  if f > 85:
      print("very satisfactory")
  if f > 75:
    print("satisfactory")
  if f > 70:
      print("fairly satisfactory")
  if f < 75:
     print("outstanding")

display_report()







