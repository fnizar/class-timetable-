from datetime import datetime, date, timedelta
def main():
    while True:
        print("\nWelcome to EduHub University Management System")
        print("1. Attendance")
        print("2. Timetable")
        print("3. Submission assignment")
        print("4. Exit")

        choice = input("Enter your choice: ")
        # If the user chooses 1
        if choice == '1':
            def take_attendance(students, class_start_time, current_time):
                # using a dictionary to store the attendance record
                attendance_record = {}
                # printing the class start time input by the user
                print("Class Start Time:", class_start_time.strftime("%I:%M %p"))
                # splitting the scenarios in the case where the difference between the class start time and the current time is more than 15 minutes
                if current_time - class_start_time > timedelta(minutes=15):
                    print(f"Attendance cannot be taken as it is more than 15 minutes past the class start time. Current time: {current_time.strftime('%I:%M %p')}")
                    # Automatically mark all students as absent
                    for student in students:
                        # Marking the student attendance as absent(0)
                        attendance_record[student] = 0
                    return attendance_record
                # In the case where the start time is within 15 minutes of the current time
                for student in students:
                    while True:
                        # Asking if the student is present at the given time using the format method (f")
                        attendance = input(f"At {class_start_time.strftime('%I:%M %p')}, is {student} present? (yes/no): ").lower()
                        if attendance == "yes":
                            # if the student is present, it will be marked as 1 in the text file
                            attendance_record[student] = 1
                            break
                        elif attendance == "no":
                            # if the student is absent, it will be marked as 0 in the text file
                            attendance_record[student] = 0
                            break
                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.")

                return attendance_record

            def calculate_attendance_percentage(attendance_records):
                attendance_percentages = []
                num_classes = len(attendance_records)

                # Count attendance for each student across all classes
                total_attendance = {student: sum(record.get(student, 0) for _, record in attendance_records) for student
                                    in
                                    set(student for _, record in attendance_records for student in record)}

                # Calculate attendance percentage for each student
                for class_name, attendance_record in attendance_records:
                    # Using a dictionary to store the attendance percentage
                    attendance_percentage = {}
                    for student, attendance in attendance_record.items():
                        if total_attendance[student] == 0:
                            attendance_percentage[student] = 0  # Setting percentage to zero if total attendance is zero
                        else:
                            attendance_percentage[student] = (attendance / total_attendance[student]) * 100
                    attendance_percentages.append((class_name, attendance_percentage))

                return attendance_percentages

            def write_attendance_to_file(attendance_records, filename):
                with open(filename, 'w') as file:
                    for class_name, attendance_record in attendance_records:
                        file.write(f"Attendance for Class {class_name}:\n")
                        for student, attendance in attendance_record.items():
                            file.write(f"{student}: {attendance}\n")
                        file.write("\n")

            def display_attendance_percentage(attendance_percentages):
                for class_name, attendance_percentage in attendance_percentages:
                    print(f"\nAttendance percentage for Class {class_name}:")
                    for student, percentage in attendance_percentage.items():
                        print(f"{student}: {percentage:.0f}%")

            if __name__ == "__main__":
                students = ["Student 1", "Student 2", "Student 3"]
                # Asking the user how many classes they would like to enter the attendance
                num_classes = int(input("How many classes do you want to record attendance for?: "))

                attendance_records = []

                for class_index in range(num_classes):
                    class_name = input(f"What is the course code for class {class_index + 1}?: ")
                    instructor_name = input(f"Who is the instructor for class {class_name}?: ")

                    while True:
                        start_time_input = input(f"What time does class {class_index + 1} start? (Format: HH:MM AM/PM): ")
                        try:
                            start_time = datetime.strptime(start_time_input, "%I:%M %p")
                            class_start_time = datetime.combine(date.today(), start_time.time())
                            current_time = datetime.now()

                            attendance = take_attendance(students, class_start_time, current_time)
                            # Only adding the record if the function returned a record
                            if attendance:
                                attendance_records.append((f"{class_name} ({instructor_name})", attendance))
                            break 
                        except ValueError:
                            print("Invalid time format. Please enter the time in the format:")

        elif choice == '2':
            class Timetable:
                def __init__(self, course_code, course_name, instructor, room_number, time_slot):
                    self.course_code = course_code
                    self.course_name = course_name
                    self.instructor = instructor
                    self.room_number = room_number
                    self.time_slot = time_slot

            timetables = []  # List to store timetable objects

            def create_timetable():
                course_code = input("Enter course code: ")
                course_name = input("Enter course name: ")
                instructor = input("Enter instructor's name: ")
                room_number = input("Enter room number: ")
                time_slot = input("Enter time slot: ")
                new_timetable = Timetable(course_code, course_name, instructor, room_number, time_slot)
                timetables.append(new_timetable)
                print("Timetable created successfully!")

            def update_timetable():
                course_code = input("Enter the course code to update: ")
                for timetable in timetables:
                    if timetable.course_code == course_code:
                        timetable.course_name = input("Enter new course name: ")
                        timetable.instructor = input("Enter new instructor's name: ")
                        timetable.room_number = input("Enter new room number: ")
                        timetable.time_slot = input("Enter new time slot: ")
                        print("Timetable updated successfully!")
                        return
                print("Course code not found.")

            def delete_timetable():
                course_code = input("Enter the course code to delete: ")
                for timetable in timetables:
                    if timetable.course_code == course_code:
                        timetables.remove(timetable)
                        print("Timetable deleted successfully!")
                        return
                print("Course code not found.")

            def display_timetables():
                for timetable in timetables:
                    print("Course Code:", timetable.course_code)
                    print("Course Name:", timetable.course_name)
                    print("Instructor:", timetable.instructor)
                    print("Room Number:", timetable.room_number)
                    print("Time Slot:", timetable.time_slot)
                    print()

            def read_timetables_from_file():
                try:
                    with open("timetables_StudentID.txt", "r") as file:
                        for line in file:
                            data = line.strip().split(",")
                            new_timetable = Timetable(*data)
                            timetables.append(new_timetable)
                except FileNotFoundError:
                    print("File 'timetables_StudentID.txt' not found. Creating a new file.")
                    # Optionally, you can create an empty file here

            def write_timetables_to_file():
                with open("timetables_StudentID.txt", "w") as file:
                    for timetable in timetables:
                        file.write(
                            f"{timetable.course_code},{timetable.course_name},{timetable.instructor},{timetable.room_number},{timetable.time_slot}\n")

            # Main program loop
            if __name__ == "__main__":
                read_timetables_from_file()
                while True:
                    print("\nWelcome to EduHub University Classroom Management System")
                    print("Manage Timetables:")
                    print("1. Create Timetable")
                    print("2. Update Timetable")
                    print("3. Delete Timetable")
                    print("4. Display Timetables")
                    print("5. Exit")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        create_timetable()
                    elif choice == '2':
                        update_timetable()
                    elif choice == '3':
                        delete_timetable()
                    elif choice == '4':
                        display_timetables()
                    elif choice == '5':
                        write_timetables_to_file()
                        print("Exiting program. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            1

            import sys
        elif choice == '3':
            def parse_list_string(list_string):
                ##converts string representation of a list into a Python list, removes leading "[" and trailing "]\n", splits the string by commas
                ##For each element in the split list, if element is solely digits, converts to integer, else removes leading and trailing quotes from it
                return [int(x) if x.strip().isdigit() else x.strip().strip("'\"") for x in
                        list_string.strip().lstrip('[').rstrip(']\n').split(',')]

            def stu_details():
                lists = []
                details = str([[10001, 'abc'], [10002, 'def'], [10003, 'ghi'], [10004, 'jkl'], [10005, 'mno']])
                f = open("Student Details.txt", "w")
                f.write(details.replace("[[", "[").replace("],", "]\n").replace("]]", "]"))
                f.close()
                f = open("Student Details.txt", "r")
                contents = f.readlines()
                f.close()
                for line in contents:
                    lists.append(parse_list_string(line))
                return lists

            def fm_details():
                lists = []
                details = str([['faculty mem 1', 'fm1']])
                f = open("Faculty Member Details.txt", "w")
                f.write(details.replace("[[", "[").replace("],", "]\n").replace("]]", "]"))
                f.close()
                f = open("Faculty Member Details.txt", "r")
                contents = f.readlines()
                f.close()
                for line in contents:
                    lists.append(parse_list_string(line))
                return lists

            def log_in():
                print("Please Log In to Proceed: \n[1] Student \n[2] Faculty Member \n[3] Exit Program")
                user_input = str(input("Please pick option [1], [2] or [3]: "))
                if user_input == "1":
                    print("\nPlease Enter Details: ")
                    stu_username = str(input("Username: "))
                    stu_password = str(input("Password: "))

                    authenticated = False
                    for sublist in studetails:
                        if stu_username == str(sublist[0]) and stu_password == str(sublist[1]):
                            print("\nLog In successful.\n")
                            authenticated = True
                            stu_menu()

                    if not authenticated:
                        print("\nError. Student username or password incorrect. \n[1] Try Again \n[2] Exit Program")
                        user_input = str(input("Please pick option [1] or [2]: "))

                        if user_input == "1":
                            print("\n")
                            log_in()
                        elif user_input == "2":
                            print("\nProgram exited. \n")
                        else:
                            print("\nError. Please pick a valid option.\n")
                            log_in()


                elif user_input == "2":
                    print("\nPlease Enter Details: ")
                    fm_username = str(input("Username: "))
                    fm_password = str(input("Password: "))

                    authenticated = False
                    for sublist in fmdetails:
                        if fm_username == str(sublist[0]) and fm_password == str(sublist[1]):
                            print("\nLog In successful.\n")
                            authenticated = True
                            fm_menu()

                    if not authenticated:
                        print("\nError. Faculty member username or password incorrect. \n[1] Try Again \n[2] Exit ")
                        user_input = str(input("Please pick option [1] or [2]: "))

                        if user_input == "1":
                            print("\n")
                            log_in()
                        elif user_input == "2":
                            print("\nProgram exited. \n")
                        else:
                            print("\nError. Please pick a valid option.\n")
                            log_in()

                elif user_input == "3":
                    print("\nProgram exited. \n")
                    sys.exit()

                else:
                    print("\nError. Please pick a valid option.\n")
                    log_in()

            def stu_menu():
                print(
                    "\nDear student, welcome to The Classroom Management System : \n[1] Mark Attendance \n[2] Manage Timetables \n[3] Submit/Check Assignments \n[4] Display \n[5]Return to log in page \n[6] Exit Program")
                user_input = str(input("Please pick option [1], [2], [3], [4], [5] or [6]: "))
                if user_input == "1":
                    stu_attendance()
                elif user_input == "2":
                    stu_timetables()
                elif user_input == "3":
                    stu_assignments()
                elif user_input == "4":
                    stu_display()
                elif user_input == "5":
                    print("\nReturning to log in page. \n")
                    log_in()
                elif user_input == "6":
                    print("\nProgram exited. \n")
                    sys.exit()
                else:
                    print("\nError. Please pick a valid option.\n")
                    stu_menu()

            ##def stu_attendance():
            ##def stu_timetables():

            def assignment_details():
                details = ["Course: MPU 3203 Appreciation of Ethic and Civilization\n\n",
                           "Submission Status: Not Submitted\n",
                           "Grading Status: Not Graded\n", "Grade(out of 100): -\n\n",
                           "Course: CSC 1024 Programming Principles\n",
                           "Submission Status: Not Submitted\n", "Grading Status: Not Graded\n",
                           "Grade(out of 100): -\n\n", """Course: MAT 1024 Linear Algebra & Applications
            \n\n""", "Submission Status: Not Submitted\n", "Grading Status: Not Graded\n", "Grade(out of 100): -\n\n",
                           "Course: BIS 1204 Electronic Commerce\n\n", "Submission Status: Not Submitted\n",
                           "Grading Status: Not Graded\n", "Grade(out of 100): -\n\n",
                           "Course: MPU 3213 Bahasa Komunikasi 2\n\n",
                           "Submission Status: Not Submitted\n", "Grading Status: Not Graded\n",
                           "Grade(out of 100): -\n\n"]
                f = open("Assignment Details.txt", "w")
                f.writelines(details)
                f.close()

            def stu_assignments():
                print(
                    "\nSubmit/Check Assignments: \n[1] Submit Assignments \n[2] Check status of submitted assignments \n[3] Return to previous page \n[4] Return to log in page")
                user_input = str(input("Please pick option [1], [2], [3] or [4]: "))
                if user_input == "1":
                    stu_submit_assignments()
                elif user_input == "2":
                    stu_check_assignments()
                elif user_input == "3":
                    print("\nReturning to previous page... \n")
                    stu_menu()
                elif user_input == "4":
                    print("\nReturning to log in page. \n")
                    log_in()
                else:
                    print("\nError. Please pick a valid option.\n")
                    stu_assignments()

            def stu_submit_assignments():
                f = open("Assignment Details.txt", "r")
                contents = f.readlines()

                result = []
                temp_course = None
                temp_students = []

                for line in contents:
                    line = line.strip()
                    if line == "":
                        if temp_course and temp_students:
                            result.append([temp_course] + temp_students)
                            temp_students = []
                    elif line.startswith("Course"):
                        if temp_course and temp_students:
                            result.append([temp_course] + temp_students)
                            temp_students = []
                        temp_course = line
                    else:
                        temp_students.append(line)

                if temp_course and temp_students:
                    result.append([temp_course] + temp_students)

                print(
                    "\nSubmit Assignment for course: \n[1] MPU 3203 Appreciation of Ethic and Civilization \n[2] CSC 1024 Programming Principles \n[3] MAT 1024 Linear Algebra & Applications \n[4] BIS 1204 Electronic Commerce \n[5] MPU 3213 Bahasa Komunikasi 2 \n[6] Return to previous page \n[7] Return to log in page")
                user_input = input("Please pick option [1], [2], [3], [4], [5], [6] or [7]: ")
                if user_input == "1":
                    for sublist in result:
                        if sublist[0] == "Course: MPU 3203 Appreciation of Ethic and Civilization":
                            for item in sublist:
                                if "Submission Status: Not Submitted" in item:
                                    upload = input("Please upload your file here (only docx and pdf files accepted): ")
                                    print()
                                    if ".docx" in upload or ".pdf" in upload:  # Check if the uploaded file is a docx or pdf file
                                        index = sublist.index(item)
                                        sublist[index] = "Submission Status: Submitted"
                                        print('\n'.join(sublist))
                                        with open("Assignment Details.txt", "w") as f:
                                            f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                        print("\nSubmission Successful. \nReturning to previous page... \n")
                                        stu_submit_assignments()  # Submission successful, exit the function
                                    else:
                                        print("Invalid file format. Only docx and pdf files are accepted.")
                                        stu_submit_assignments()
                            else:
                                print('\n'.join(sublist))
                                print(
                                    "\nA submission for this assignment has already been made. \nReturning to previous page... \n")
                                stu_submit_assignments()  # Submission already made, exit the function
                    else:
                        print("Course not found.")

                elif user_input == "2":
                    for sublist in result:
                        if sublist[0] == "Course: CSC 1024 Programming Principles":
                            for item in sublist:
                                if "Submission Status: Not Submitted" in item:
                                    upload = input("Please upload your file here (only docx and pdf files accepted): ")
                                    print()
                                    if ".docx" in upload or ".pdf" in upload:  # Check if the uploaded file is a docx or pdf file
                                        index = sublist.index(item)
                                        sublist[index] = "Submission Status: Submitted"
                                        print('\n'.join(sublist))
                                        with open("Assignment Details.txt", "w") as f:
                                            f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                        print("\nSubmission Successful. \nReturning to previous page... \n")
                                        stu_submit_assignments()  # Submission successful, exit the function
                                    else:
                                        print("Invalid file format. Only docx and pdf files are accepted.")
                                        stu_submit_assignments()
                            else:
                                print('\n'.join(sublist))
                                print(
                                    "\nA submission for this assignment has already been made. \nReturning to previous page... \n")
                                stu_submit_assignments()  # Submission already made, exit the function
                    else:
                        print("Course not found.")

                elif user_input == "3":
                    for sublist in result:
                        if sublist[0] == """Course: MAT 1024 Linear Algebra & Applications
            """:
                            for item in sublist:
                                if "Submission Status: Not Submitted" in item:
                                    upload = input("Please upload your file here (only docx and pdf files accepted): ")
                                    print()
                                    if ".docx" in upload or ".pdf" in upload:  # Check if the uploaded file is a docx or pdf file
                                        index = sublist.index(item)
                                        sublist[index] = "Submission Status: Submitted"
                                        print('\n'.join(sublist))
                                        with open("Assignment Details.txt", "w") as f:
                                            f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                        print("\nSubmission Successful. \nReturning to previous page... \n")
                                        stu_submit_assignments()  # Submission successful, exit the function
                                    else:
                                        print("Invalid file format. Only docx and pdf files are accepted.")
                                        stu_submit_assignments()
                            else:
                                print('\n'.join(sublist))
                                print(
                                    "\nA submission for this assignment has already been made. \nReturning to previous page... \n")
                                stu_submit_assignments()  # Submission already made, exit the function
                    else:
                        print("Course not found.")

                elif user_input == "Course: BIS 1204 Electronic Commerce":
                    for sublist in result:
                        if sublist[0] == 'Course04, Assignment 1':
                            for item in sublist:
                                if "Submission Status: Not Submitted" in item:
                                    upload = input("Please upload your file here (only docx and pdf files accepted): ")
                                    print()
                                    if ".docx" in upload or ".pdf" in upload:  # Check if the uploaded file is a docx or pdf file
                                        index = sublist.index(item)
                                        sublist[index] = "Submission Status: Submitted"
                                        print('\n'.join(sublist))
                                        with open("Assignment Details.txt", "w") as f:
                                            f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                        print("\nSubmission Successful. \nReturning to previous page... \n")
                                        stu_submit_assignments()  # Submission successful, exit the function
                                    else:
                                        print("Invalid file format. Only docx and pdf files are accepted.")
                                        stu_submit_assignments()
                            else:
                                print('\n'.join(sublist))
                                print(
                                    "\nA submission for this assignment has already been made. \nReturning to previous page... \n")
                                stu_submit_assignments()  # Submission already made, exit the function
                    else:
                        print("Course not found.")

                elif user_input == "5":
                    for sublist in result:
                        if sublist[0] == 'Course: MPU 3213 Bahasa Komunikasi 2':
                            for item in sublist:
                                if "Submission Status: Not Submitted" in item:
                                    upload = input("Please upload your file here (only docx and pdf files accepted): ")
                                    print()
                                    if ".docx" in upload or ".pdf" in upload:  # Check if the uploaded file is a docx or pdf file
                                        index = sublist.index(item)
                                        sublist[index] = "Submission Status: Submitted"
                                        print('\n'.join(sublist))
                                        with open("Assignment Details.txt", "w") as f:
                                            f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                        print("\nSubmission Successful. \nReturning to previous page... \n")
                                        stu_submit_assignments()  # Submission successful, exit the function
                                    else:
                                        print("Invalid file format. Only docx and pdf files are accepted.")
                                        stu_submit_assignments()
                            else:
                                print('\n'.join(sublist))
                                print(
                                    "\nA submission for this assignment has already been made. \nReturning to previous page... \n")
                                stu_submit_assignments()  # Submission already made, exit the function
                    else:
                        print("Course not found.")

                elif user_input == "6":
                    print("\nReturning to previous page... \n")
                    stu_assignments()

                elif user_input == "7":
                    print("\nReturning to log in page. \n")
                    log_in()

                else:
                    print("\nError. Please pick a valid option. \n")
                    stu_submit_assignments()

            def stu_check_assignments():
                f = open("Assignment Details.txt", "r")
                contents = f.read()
                f.close()
                print(contents)
                while True:
                    print("\nWould you like to \n[1] Return to previous page \n[2] Return to log in page")
                    user_input = input("Please pick option [1] or [2]: ")

                    if user_input == "1":
                        print("\nReturning to previous page... \n")
                        stu_assignments()
                    elif user_input == "2":
                        print("\nReturning to log in page. \n")
                        log_in()
                    else:
                        print("\nError. Please pick a valid option. \n")

            def stu_display():
                print(
                    "\nDisplay: \n[1] Attendance \n[2] Timetables \n[3] Assignments \n[4] Return to previous page \n[5] Return to log in page")
                user_input = str(input("Please pick option [1], [2], [3], [4] or [5]: "))
                if user_input == "1":
                    display_attendance()
                elif user_input == "2":
                    display_timetables
                elif user_input == "3":
                    stu_check_assignments()
                elif user_input == "4":
                    print("\nReturning to previous page... \n")
                    stu_menu()
                elif user_input == "5":
                    print("\nReturning to log in page. \n")
                    log_in()
                else:
                    print("\nError. Please pick a valid option. \n")
                    stu_display()

            def fm_menu():
                print(
                    "\nDear faculty member, welcome to The Classroom Management System : \n[1] Mark Attendance \n[2] Manage Timetables \n[3] Grade/Check Assignments \n[4] Display \n[5] Return to log in page ")
                user_input = str(input("Please pick option [1], [2], [3], [4] or [5]: "))
                if user_input == "1":
                    fm_attendance()
                elif user_input == "2":
                    fm_timetables()
                elif user_input == "3":
                    fm_assignments()
                elif user_input == "4":
                    fm_display()
                elif user_input == "5":
                    print("\nReturning to log in page. \n")
                    log_in()
                else:
                    print("\nError. Please pick a valid option. \n")
                    fm_menu()

            def fm_assignments():
                print(
                    "\nGrade/Check Assignments: \n[1] Grade Assignments \n[2] Check status of submitted assignments \n[3] Return to previous page \n[4] Return to log in page")
                user_input = str(input("Please pick option [1], [2], [3] or [4]: "))
                if user_input == "1":
                    fm_grade_assignments()
                elif user_input == "2":
                    fm_check_assignments()
                elif user_input == "3":
                    print("\nReturning to previous page... \n")
                    fm_menu()
                elif user_input == "4":
                    print("\nReturning to log in page. \n")
                    log_in()
                else:
                    print("\nError. Please pick a valid option.\n")
                    fm_assignments()

            def fm_grade_assignments():
                f = open("Assignment Details.txt", "r")
                contents = f.readlines()

                result = []
                temp_course = None
                temp_students = []

                for line in contents:
                    line = line.strip()
                    if line == "":
                        if temp_course and temp_students:
                            result.append([temp_course] + temp_students)
                            temp_students = []
                    elif line.startswith("Course"):
                        if temp_course and temp_students:
                            result.append([temp_course] + temp_students)
                            temp_students = []
                        temp_course = line
                    else:
                        temp_students.append(line)

                if temp_course and temp_students:
                    result.append([temp_course] + temp_students)

                print(
                    "\nGrade Assignment for course: \n[1] MPU 3203 Appreciation of Ethic and Civilization \n[2] CSC 1024 Programming Principles \n[3] MAT 1024 Linear Algebra & Applications \n[4] BIS 1204 Electronic Commerce \n[5]MPU 3213 Bahasa Komunikasi 2 \n[6] Return to previous page \n[7] Return to log in page")
                user_input = input("Please pick option [1], [2], [3], [4], [5], [6] or [7]: ")
                if user_input == "1":
                    for sublist in result:
                        if sublist[0] == 'Course: MPU 3203 Appreciation of Ethic and Civilization':
                            if "Submission Status: Submitted" in sublist:
                                if "Grading Status: Not Graded" in sublist:
                                    grade = input("Please enter the grade given (out of 100): ")
                                    print()
                                    try:
                                        grade = int(grade)
                                        if 0 <= grade <= 100:
                                            index = sublist.index("Grading Status: Not Graded")
                                            sublist[index] = "Grading Status: Graded"
                                            # Remove the placeholder line if present
                                            if "Grade(out of 100): -" in sublist:
                                                sublist.remove("Grade(out of 100): -")
                                            sublist.append(
                                                f"Grade(out of 100): {grade}")  # Append the grade information
                                            print('\n'.join(sublist))  # Print updated assignment details
                                            with open("Assignment Details.txt", "w") as f:
                                                f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                            print("\nGrading Successful. \nReturning to previous page... \n")
                                            fm_grade_assignments()  # Grading successful, exit to previous page
                                        else:
                                            print("Invalid grade. Grade should be between 0 to 100.")
                                            fm_grade_assignments()
                                    except ValueError:
                                        print("Invalid input. Please enter a valid grade.")
                                        fm_grade_assignments()
                                else:
                                    print('\n'.join(sublist))
                                    print(
                                        "\nThis assignment has already been graded. \nReturning to previous page... \n")
                                    fm_grade_assignments()  # Submission already made, exit to previous page
                            else:
                                print(
                                    "\nThere is no submission for this assignment. \nReturning to previous page... \n")
                                fm_grade_assignments()
                    else:
                        print("Course not found.")
                        fm_grade_assignments()

                elif user_input == "2":
                    for sublist in result:
                        if sublist[0] == 'Course: CSC 1024 Programming Principles':
                            if "Submission Status: Submitted" in sublist:
                                if "Grading Status: Not Graded" in sublist:
                                    grade = input("Please enter the grade given (out of 100): ")
                                    print()
                                    try:
                                        grade = int(grade)
                                        if 0 <= grade <= 100:
                                            index = sublist.index("Grading Status: Not Graded")
                                            sublist[index] = "Grading Status: Graded"
                                            # Remove the placeholder line if present
                                            if "Grade(out of 100): -" in sublist:
                                                sublist.remove("Grade(out of 100): -")
                                            sublist.append(
                                                f"Grade(out of 100): {grade}")  # Append the grade information
                                            print('\n'.join(sublist))  # Print updated assignment details
                                            with open("Assignment Details.txt", "w") as f:
                                                f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                            print("\nGrading Successful. \nReturning to previous page... \n")
                                            fm_grade_assignments()  # Grading successful, exit to previous page
                                        else:
                                            print("Invalid grade. Grade should be between 0 to 100.")
                                            fm_grade_assignments()
                                    except ValueError:
                                        print("Invalid input. Please enter a valid grade.")
                                        fm_grade_assignments()
                                else:
                                    print('\n'.join(sublist))
                                    print(
                                        "\nThis assignment has already been graded. \nReturning to previous page... \n")
                                    fm_grade_assignments()  # Submission already made, exit to previous page
                            else:
                                print(
                                    "\nThere is no submission for this assignment. \nReturning to previous page... \n")
                                fm_grade_assignments()
                    else:
                        print("Course not found.")
                        fm_grade_assignments()

                elif user_input == "3":
                    for sublist in result:
                        if sublist[0] == """Course: MAT 1024 Linear Algebra & Applications""":
                            if "Submission Status: Submitted" in sublist:
                                if "Grading Status: Not Graded" in sublist:
                                    grade = input("Please enter the grade given (out of 100): ")
                                    print()
                                    try:
                                        grade = int(grade)
                                        if 0 <= grade <= 100:
                                            index = sublist.index("Grading Status: Not Graded")
                                            sublist[index] = "Grading Status: Graded"
                                            # Remove the placeholder line if present
                                            if "Grade(out of 100): -" in sublist:
                                                sublist.remove("Grade(out of 100): -")
                                            sublist.append(
                                                f"Grade(out of 100): {grade}")  # Append the grade information
                                            print('\n'.join(sublist))  # Print updated assignment details
                                            with open("Assignment Details.txt", "w") as f:
                                                f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                            print("\nGrading Successful. \nReturning to previous page... \n")
                                            fm_grade_assignments()  # Grading successful, exit to previous page
                                        else:
                                            print("Invalid grade. Grade should be between 0 to 100.")
                                            fm_grade_assignments()
                                    except ValueError:
                                        print("Invalid input. Please enter a valid grade.")
                                        fm_grade_assignments()
                                else:
                                    print('\n'.join(sublist))
                                    print(
                                        "\nThis assignment has already been graded. \nReturning to previous page... \n")
                                    fm_grade_assignments()  # Submission already made, exit to previous page
                            else:
                                print(
                                    "\nThere is no submission for this assignment. \nReturning to previous page... \n")
                                fm_grade_assignments()
                    else:
                        print("Course not found.")
                        fm_grade_assignments()

                if user_input == "4":
                    for sublist in result:
                        if sublist[0] == 'Course: BIS 1204 Electronic Commerce':
                            if "Submission Status: Submitted" in sublist:
                                if "Grading Status: Not Graded" in sublist:
                                    grade = input("Please enter the grade given (out of 100): ")
                                    print()
                                    try:
                                        grade = int(grade)
                                        if 0 <= grade <= 100:
                                            index = sublist.index("Grading Status: Not Graded")
                                            sublist[index] = "Grading Status: Graded"
                                            # Remove the placeholder line if present
                                            if "Grade(out of 100): -" in sublist:
                                                sublist.remove("Grade(out of 100): -")
                                            sublist.append(
                                                f"Grade(out of 100): {grade}")  # Append the grade information
                                            print('\n'.join(sublist))  # Print updated assignment details
                                            with open("Assignment Details.txt", "w") as f:
                                                f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                            print("\nGrading Successful. \nReturning to previous page... \n")
                                            fm_grade_assignments()  # Grading successful, exit to previous page
                                        else:
                                            print("Invalid grade. Grade should be between 0 to 100.")
                                            fm_grade_assignments()
                                    except ValueError:
                                        print("Invalid input. Please enter a valid grade.")
                                        fm_grade_assignments()
                                else:
                                    print('\n'.join(sublist))
                                    print(
                                        "\nThis assignment has already been graded. \nReturning to previous page... \n")
                                    fm_grade_assignments()  # Submission already made, exit to previous page
                            else:
                                print(
                                    "\nThere is no submission for this assignment. \nReturning to previous page... \n")
                                fm_grade_assignments()
                    else:
                        print("Course not found.")
                        fm_grade_assignments()

                elif user_input == "5":
                    for sublist in result:
                        if sublist[0] == 'Course: MPU 3213 Bahasa Komunikasi 2':
                            if "Submission Status: Submitted" in sublist:
                                if "Grading Status: Not Graded" in sublist:
                                    grade = input("Please enter the grade given (out of 100): ")
                                    print()
                                    try:
                                        grade = int(grade)
                                        if 0 <= grade <= 100:
                                            index = sublist.index("Grading Status: Not Graded")
                                            sublist[index] = "Grading Status: Graded"
                                            # Remove the placeholder line if present
                                            if "Grade(out of 100): -" in sublist:
                                                sublist.remove("Grade(out of 100): -")
                                            sublist.append(
                                                f"Grade(out of 100): {grade}")  # Append the grade information
                                            print('\n'.join(sublist))  # Print updated assignment details
                                            with open("Assignment Details.txt", "w") as f:
                                                f.write('\n\n'.join('\n'.join(sublist) for sublist in result))
                                            print("\nGrading Successful. \nReturning to previous page... \n")
                                            fm_grade_assignments()  # Grading successful, exit to previous page
                                        else:
                                            print("Invalid grade. Grade should be between 0 to 100.")
                                            fm_grade_assignments()
                                    except ValueError:
                                        print("Invalid input. Please enter a valid grade.")
                                        fm_grade_assignments()
                                else:
                                    print('\n'.join(sublist))
                                    print(
                                        "\nThis assignment has already been graded. \nReturning to previous page... \n")
                                    fm_grade_assignments()  # Submission already made, exit to previous page
                            else:
                                print(
                                    "\nThere is no submission for this assignment. \nReturning to previous page... \n")
                                fm_grade_assignments()
                    else:
                        print("Course not found.")
                        fm_grade_assignments()

                elif user_input == "6":
                    print("\nReturning to previous page... \n")
                    fm_assignments()

                elif user_input == "7":
                    print("\nReturning to log in page. \n")
                    log_in()

                else:
                    print("\nError. Please pick a valid option. \n")
                    fm_grade_assignments()

            def fm_check_assignments():
                f = open("Assignment Details.txt", "r")
                contents = f.read()
                f.close()
                print(contents)
                while True:
                    print("\nWould you like to \n[1] Return to previous page \n[2] Return to log in page")
                    user_input = input("Please pick option [1] or [2]: ")

                    if user_input == "1":
                        print("\nReturning to previous page... \n")
                        fm_assignments()
                    elif user_input == "2":
                        print("\nReturning to log in page. \n")
                        log_in()
                    else:
                        print("\nError. Please pick a valid option. \n")

            def fm_display():
                print(
                    "\nDisplay: \n[1] Attendance \n[2] Timetables \n[3] Assignments \n[4] Return to previous page \n[5] Return to log in page")
                user_input = str(input("Please pick option [1], [2], [3], [4] or [5]: "))
                if user_input == "1":
                    display_attendance()
                elif user_input == "2":
                    display_timetables()
                elif user_input == "3":
                    fm_check_assignments()
                elif user_input == "4":
                    print("\nReturning to previous page... \n")
                    fm_menu()
                elif user_input == "5":
                    print("\nReturning to log in page. \n")
                    log_in()
                else:
                    print("\nError. Please pick a valid option. \n")
                    fm_display()

            assignment_details()  ##comment out when running second time for faculty
            studetails = stu_details()
            stu_details()
            fmdetails = fm_details()
            fm_details()
            log_in()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




