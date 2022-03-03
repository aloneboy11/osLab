grades = []
for i in range(3):
    name = input("نام درس: ")
    grade = float(input("نمره: "))
    grades.append(grade)
avg = sum(grades) / 3
print("معدل شما: ", round(avg, 2))
