# Student grades

student_scores = {
    "AM": 90,
    "SM": 83,
    "HM": 89,
    "DM": 79,
}

student_grades = {}


for student in student_scores:
    mark = student_scores[student]
    if mark >= 90:
        student_grades[student] = "Outstanding"
    elif mark >= 80:
        student_grades[student] = "Above expectations"
    elif mark >= 70:
        student_grades[student] = "Tried"
    else:
        student_grades[student] = "Fail"


print(student_grades)
