

grade = []

quiz1 = int(input("Enter Quiz 1: "))
grade.append(quiz1)

quiz2 = int(input("Enter Quiz 2: "))
grade.append(quiz2)
quiz3 = int(input("Enter Quiz 3: "))
grade.append(quiz3)
quiz4 = int(input("Enter Quiz 4: "))
grade.append(quiz4)
quiz5 = int(input("Enter Quiz 5: "))
grade.append(quiz5)
quiz = len(grade)
total = sum(grade)
average = total / quiz
lowest = min(grade)
highest = max(grade)

Ascending = sorted(grade)
Descending = sorted(grade, reverse=True)
print("==========quiz score analyzer============")
print(grade)
print("Number of Quizzes: ", quiz)
print ("Total Score", total)
print("Average Score", average)
print("Lowest Score", lowest)
print("Highest Score", highest)
print("Descending", Descending)
print("Ascending", Ascending)
print("Original: ", grade )


