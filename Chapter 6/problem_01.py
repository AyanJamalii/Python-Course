# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks_1 = int(input("Enter yours marks 1: "))
marks_2 = int(input("Enter yours marks 2: "))
marks_3 = int(input("Enter yours marks 3: "))

total_percentage = (100*(marks_1 + marks_2 + marks_3))/300

if(total_percentage > 40 and marks_1>=33 and marks_2>=33 and marks_3>=33):
    print(f"Congrats! You're Pass, your percentage is: {total_percentage}")
else:
    print("Sorry! You're Failed.", total_percentage)