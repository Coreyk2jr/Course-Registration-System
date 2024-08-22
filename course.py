import sys

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            if len(course.students) < course.max_capacity:
                self.courses.append(course)
                course.add_student(self)
                print(f"Enrollment successful: {self.name} enrolled in {course.course_code} - {course.title}")
            else:
                print(f"Cannot enroll {self.name} in {course.course_code}. Course is full.")
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
        # Add pre-installed courses
        self.pre_install_courses()

    def pre_install_courses(self):
        pre_installed_courses = [
            {"course_code": "CS101", "title": "Introduction to Computer Science", "max_capacity": 30},
            {"course_code": "MATH101", "title": "Calculus I", "max_capacity": 25},
            {"course_code": "ENG101", "title": "English Literature", "max_capacity": 20},
            {"course_code": "BIO101", "title": "Biology 101", "max_capacity": 30}
        ]
        for course in pre_installed_courses:
            self.courses[course["course_code"]] = Course(course["course_code"], course["title"], course["max_capacity"])
        print("Pre-installed courses have been added.")

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
            try:
                max_capacity = int(input("Enter maximum capacity: ").strip())
                if max_capacity <= 0:
                    print("Error: Maximum capacity must be a positive number.")
                    return
            except ValueError:
                print("Error: Please enter a valid number for maximum capacity.")
                return
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
    university_db = UniversityDatabaseCLI()
    university_db.run()

