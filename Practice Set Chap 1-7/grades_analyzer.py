students_data = []
total_students = int(input("Enter the total amount of Students: "))

for i in range(total_students):
    print(f"\n Students {i+1}'s Data: ")

    name = input("Enter your name: ")
    marks_1 = int(input("Enter the number of Subject 1: "))
    marks_2 = int(input("Enter the number of Subject 2: "))
    marks_3 = int(input("Enter the number of Subject 3: "))
    total_percentage = 100*(marks_1 + marks_2 + marks_3)/300

    grade = ''

    if (total_percentage>40 and marks_1>= 33 and marks_2>= 33 and marks_3>= 33):
        if(90 <= total_percentage <= 100):
            grade = "Ex (A+)"
        elif(80 <= total_percentage < 90):
            grade = "A"
        elif(70 <= total_percentage < 80):
            grade = "B"
        elif(60 <= total_percentage < 70):
            grade = "C"
        elif(50 <= total_percentage < 60):
            grade = "D"
        else:
            grade = "E (Just Passed.)"
        print(f"Congrats {name}, You're Grade is {grade}")
    else: 
        grade = "F (Fail)"
        print(f"{name}, You're Failed.")
    students_data.append({"name": name, "percentage": total_percentage, "Grade": grade})