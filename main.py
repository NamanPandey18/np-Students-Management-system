import json
import os

def main_menu():
    print("========================================")
    heading="STUDENT MANAGEMENT SYSTEM"
    print(heading.center(40))
    print("========================================")
    print("Add Student              - Enter 1")
    print("Display All Students     - Enter 2")
    print("Search Student           - Enter 3")
    print("Update Student           - Enter 4")
    print("Delete Student           - Enter 5")
    print("Student Marks            - Enter 6")
    print("Calculate Result         - Enter 7")
    print("View Class-wise Students - Enter 8")
    print("Exit                     - Enter 9")
    print("========================================")

def load_students():
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            return json.load(file)

    return []

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()

    print("\n--- Add Student ---")

    roll_no = input("Enter Roll Number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Error: Roll number already exists!")
            return

    name = input("Enter Student Name: ")
    student_class = input("Enter Class: ")
    contact = input("Enter Contact Number: ")

    student = {
        "roll_no": roll_no,
        "name": name,
        "class": student_class,
        "contact": contact
    }
    students.append(student)
    save_students(students)

    print("Student added successfully!")

def display_students():
    students = load_students()

    if students:
        for i in students:
            for j in i:
                print(j, ":", i[j])
            print("-------------------")
    else:
        print("There is no information of any student")

def search_student():
    students = load_students()
    roll_no = input("Enter Roll Number: ")
    for student in students:
        if student["roll_no"]==roll_no:
            print("Student Found")
            print("Student's information")
            for info in student:
                print(info,":",student[info])
            return
            
    print("Student not found")

def update_student():
    students = load_students()
    roll_no = input("Enter Roll Number to Update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student Found!")
            print("Now you can update information.")

            name = input("Enter New Name: ")
            student_class = input("Enter New Class: ")
            contact = input("Enter New Contact Number: ")
        
            if name:
                student["name"] = name

            if student_class:
                student["class"] = student_class

            if contact:
                student["contact"] = contact
                print("Updated successfully")
                save_students(students)
            return

    print("Student not found.")

def delete_student():
    students = load_students()
    roll_no = input("Enter Roll Number to delete: ")
    
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student Found!")
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return
        
    print("Student not found.")
    
def student_marks():
    students = load_students()

    print("\n--- Add Student's Marks ---")

    roll_no = input("Enter Roll Number: ")
    found = False

    for student in students:
        if student["roll_no"] == roll_no:
            found = True
            print("Student Found! You can add marks.")

            subjects = [
                "English",
                "Hindi",
                "Physics",
                "Chemistry",
                "Mathematics",
                "Computer_Science"
            ]

            marks = {}
            for subject in subjects:
                while True:
                    try:
                        mark = int(input(f"Enter marks of {subject}: "))

                        if 0 <= mark <= 100:
                            marks[subject] = mark
                            break
                        else:
                            print("Invalid marks! Enter marks between 0 and 100.")

                    except ValueError:
                        print("Invalid input! Enter numbers only.")

            student["marks"] = marks
            save_students(students)

            print("Student's marks added successfully!")

            return

    if not found:
        print("Student not found!")

def calculate_result():
    students = load_students()

    roll_no = input("Enter Roll Number to Calculate Result: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\n--- Student Result ---")
            print("Student Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Class:", student["class"])

            if "marks" not in student or not student["marks"]:
                print("Marks have not been entered yet!")
                return

            marks = student["marks"]

            if not all(
                isinstance(mark, int) and 0 <= mark <= 100
                for mark in marks.values()
            ):
                print("Result cannot be calculated. Invalid marks found.")
                return

            total = sum(marks.values())
            total_subjects = len(marks)
            maximum_marks = total_subjects * 100
            percentage = (total / maximum_marks) * 100

            print("\n--- Subject-wise Marks ---")

            for subject, mark in marks.items():
                print(subject, ":", mark)

            print("--------------------------")
            print("Total Marks:", total, "/", maximum_marks)
            print("Percentage:", round(percentage, 2), "%")

            if all(mark >= 33 for mark in marks.values()):
                print("Result: PASS")
            else:
                print("Result: FAIL")

            return

    print("Student not found!")

def view_students_classwise():
    students = load_students()
    classr = input("Enter Class: ")
    found = False
    for student in students:
        if student["class"]==classr:
            found=True
            for info in student:
                print(info,":",student[info])
            print("-------------------")
    if not found:
        print("No student found in this Class!!")

while True:
    main_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Add Student Selected")
        add_student()

    elif choice == "2":
        print("Display Students Selected")
        print("-------------------")
        display_students()

    elif choice == "3":
        print("Search Student Selected")
        search_student()

    elif choice == "4":
        print("Update Student Selected")
        update_student()

    elif choice == "5":
        print("Delete Student Selected")
        delete_student()

    elif choice == "6":
        print("Enter Student Marks Selected")
        student_marks()

    elif choice == "7":
        print("Calculate Result Selected")
        calculate_result()

    elif choice == "8":
        print("Class-wise Students Selected")
        view_students_classwise()

    elif choice == "9":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice ! Please try again.")