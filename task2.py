courses = {"Python", "Java", "MERN", "Data Science"}

enrollments = [
    (1, "mishal", "Python"),
    (2, "muhammed", "Java")
]

while True:
    print("\nCourse Enrollment System")
    print("1. Add Enrollment")
    print("2. View All Enrollments")
    print("3. View Enrollments By Course")
    print("4. Update Course")
    print("5. Delete Enrollment")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        student_id = int(input("Enter Student ID: "))
        student_name = input("Enter Student Name: ")
        course_name = input("Enter Course Name: ")

        id_exists = False
        duplicate = False

        for e in enrollments:
            if e[0] == student_id:
                id_exists = True
            if e[1] == student_name and e[2] == course_name:
                duplicate = True

        if course_name not in courses:
            print("Course does not exist")
        elif id_exists:
            print("Student ID already exists")
        elif duplicate:
            print("Student already enrolled in this course")
        else:
            enrollments.append((student_id, student_name, course_name))
            print("Enrollment added successfully")

    
    elif choice == 2:
        print("\nID  Name   Course")
        for e in enrollments:
            print(e[0], e[1], e[2])

   
    elif choice == 3:
        course_name = input("Enter course name: ")
        print(f"\nStudents enrolled in {course_name}:")
        for e in enrollments:
            if e[2] == course_name:
                print(e[1])

    
    elif choice == 4:
        student_id = int(input("Enter Student ID: "))
        new_course = input("Enter new course name: ")

        found = False

        if new_course not in courses:
            print("Course does not exist")
        else:
            for i in range(len(enrollments)):
                if enrollments[i][0] == student_id:
                    enrollments[i] = (enrollments[i][0], enrollments[i][1], new_course)
                    found = True
                    print("Course updated successfully")
                    break

            if not found:
                print("Student not found")

    
    elif choice == 5:
        student_id = int(input("Enter Student ID: "))
        found = False

        for e in enrollments:
            if e[0] == student_id:
                enrollments.remove(e)
                found = True
                print("Enrollment removed successfully")
                break

        if not found:
            print("Student not found")

    
    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")