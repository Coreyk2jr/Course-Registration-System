import sys

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = [] 

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
            print(f"Enrollment successful: {self.name} enrolled in {course.course_code} - {course.title}")
        else:
            print(f"{self.name} is already enrolled in {course.course_code}")

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.remove_student(self)
            print(f"{self.name} has dropped {course.course_code} - {course.title}")
        else:
            print(f"{self.name} is not enrolled in {course.course_code}")

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}"


class Course:
    def __init__(self, course_code, title, max_capacity):
        self.course_code = course_code
        self.title = title
        self.max_capacity = max_capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_capacity:
            self.students.append(student)
        else:
            print(f"Cannot add {student.name} to {self.course_code}. Maximum capacity reached.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def __str__(self):
        return f"Course Code: {self.course_code}, Title: {self.title}, Capacity: {len(self.students)}/{self.max_capacity}"


class UniversityDatabaseCLI:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ").strip().lower()
            if choice == '1':
                self.register_student()
            elif choice == '2':
                self.add_course()
            elif choice == '3':
                self.enroll_student()
            elif choice == '4':
                self.drop_student()
            elif choice == '5':
                self.print_students()
            elif choice == '6':
                self.print_courses()
            elif choice == '7':
                print("Exiting program. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please enter a number from the menu.")

    def print_menu(self):
        menu = """
        University Database System Menu:
        1. Register a new student
        2. Add a new course
        3. Enroll a student in a course
        4. Drop a student from a course
        5. Print all students
        6. Print all courses
        7. Exit
        """
        print(menu)

    def register_student(self):
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()
        if student_id in self.students:
            print(f"Error: Student with ID '{student_id}' already exists.")
        else:
            self.students[student_id] = Student(student_id, name)
            print(f"Student registered successfully: {name}")

    def add_course(self):
        course_code = input("Enter course code: ").strip().upper()
        if course_code in self.courses:
            print(f"Error: Course with code '{course_code}' already exists.")
        else:
            title = input("Enter course title: ").strip()
            max_capacity = int(input("Enter maximum capacity: ").strip())
            self.courses[course_code] = Course(course_code, title, max_capacity)
            print(f"Course added successfully: {course_code} - {title}")

    def enroll_student(self):
        student_id = input("Enter student ID: ").strip()
        course_code = input("Enter course code: ").strip().upper()
        if student_id not in self.students:
            print(f"Error: Student with ID '{student_id}' not found.")
        elif course_code not in self.courses:
            print(f"Error: Course with code '{course_code}' not found.")
        else:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll(course)

    def drop_student(self):
        student_id = input("Enter student ID: ").strip()
        course_code = input("Enter course code: ").strip().upper()
        if student_id not in self.students:
            print(f"Error: Student with ID '{student_id}' not found.")
        elif course_code not in self.courses:
            print(f"Error: Course with code '{course_code}' not found.")
        else:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.drop(course)

    def print_students(self):
        print("List of Students:")
        for student in self.students.values():
            print(student)

    def print_courses(self):
        print("List of Courses:")
        for course in self.courses.values():
            print(course)


if __name__ == "__main__":
    # Initialize and run the UniversityDatabaseCLI
    university_db = UniversityDatabaseCLI()
    university_db.run()
