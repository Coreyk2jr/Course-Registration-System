import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

class Student {
    private String studentId;
    private String name;
    private ArrayList<Course> courses;

    public Student(String studentId, String name) {
        this.studentId = studentId;
        this.name = name;
        this.courses = new ArrayList<>();
    }

    public void enroll(Course course) {
        if (!courses.contains(course)) {
            if (course.getStudents().size() < course.getMaxCapacity()) {
                courses.add(course);
                course.addStudent(this);
                System.out.println("Enrollment successful: " + name + " enrolled in " + course.getCourseCode() + " - " + course.getTitle());
            } else {
                System.out.println("Cannot enroll " + name + " in " + course.getCourseCode() + ". Course is full.");
            }
        } else {
            System.out.println(name + " is already enrolled in " + course.getCourseCode());
        }
    }

    public void drop(Course course) {
        if (courses.contains(course)) {
            courses.remove(course);
            course.removeStudent(this);
            System.out.println(name + " has dropped " + course.getCourseCode() + " - " + course.getTitle());
        } else {
            System.out.println(name + " is not enrolled in " + course.getCourseCode());
        }
    }

    @Override
    public String toString() {
        return "Student ID: " + studentId + ", Name: " + name;
    }
}

class Course {
    private String courseCode;
    private String title;
    private int maxCapacity;
    private ArrayList<Student> students;

    public Course(String courseCode, String title, int maxCapacity) {
        this.courseCode = courseCode;
        this.title = title;
        this.maxCapacity = maxCapacity;
        this.students = new ArrayList<>();
    }

    public void addStudent(Student student) {
        if (students.size() < maxCapacity) {
            students.add(student);
        } else {
            System.out.println("Cannot add " + student + " to " + courseCode + ". Maximum capacity reached.");
        }
    }

    public void removeStudent(Student student) {
        students.remove(student);
    }

    public String getCourseCode() {
        return courseCode;
    }

    public String getTitle() {
        return title;
    }

    public int getMaxCapacity() {
        return maxCapacity;
    }

    public ArrayList<Student> getStudents() {
        return students;
    }

    @Override
    public String toString() {
        return "Course Code: " + courseCode + ", Title: " + title + ", Capacity: " + students.size() + "/" + maxCapacity;
    }
}

class UniversityDatabaseCLI {
    private HashMap<String, Student> students;
    private HashMap<String, Course> courses;

    public UniversityDatabaseCLI() {
        students = new HashMap<>();
        courses = new HashMap<>();
        preInstallCourses();
    }

    private void preInstallCourses() {
        String[][] preInstalledCourses = {
            {"CS101", "Introduction to Computer Science", "30"},
            {"MATH101", "Calculus I", "25"},
            {"ENG101", "English Literature", "20"},
            {"BIO101", "Biology 101", "30"}
        };

        for (String[] courseData : preInstalledCourses) {
            courses.put(courseData[0], new Course(courseData[0], courseData[1], Integer.parseInt(courseData[2])));
        }
        System.out.println("Pre-installed courses have been added.");
    }

    public void run() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            printMenu();
            String choice = scanner.nextLine().trim();
            switch (choice) {
                case "1":
                    registerStudent(scanner);
                    break;
                case "2":
                    addCourse(scanner);
                    break;
                case "3":
                    enrollStudent(scanner);
                    break;
                case "4":
                    dropStudent(scanner);
                    break;
                case "5":
                    printStudents();
                    break;
                case "6":
                    printCourses();
                    break;
                case "7":
                    System.out.println("Exiting program. Goodbye!");
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a number from the menu.");
            }
        }
    }

    private void printMenu() {
        System.out.println("""
            University Database System Menu:
            1. Register a new student
            2. Add a new course
            3. Enroll a student in a course
            4. Drop a student from a course
            5. Print all students
            6. Print all courses
            7. Exit
            """);
    }

    private void registerStudent(Scanner scanner) {
        System.out.print("Enter student ID: ");
        String studentId = scanner.nextLine().trim();
        System.out.print("Enter student name: ");
        String name = scanner.nextLine().trim();
        if (students.containsKey(studentId)) {
            System.out.println("Error: Student with ID '" + studentId + "' already exists.");
        } else {
            students.put(studentId, new Student(studentId, name));
            System.out.println("Student registered successfully: " + name);
        }
    }

    private void addCourse(Scanner scanner) {
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine().trim().toUpperCase();
        if (courses.containsKey(courseCode)) {
            System.out.println("Error: Course with code '" + courseCode + "' already exists.");
        } else {
            System.out.print("Enter course title: ");
            String title = scanner.nextLine().trim();
            System.out.print("Enter maximum capacity: ");
            int maxCapacity = Integer.parseInt(scanner.nextLine().trim());
            courses.put(courseCode, new Course(courseCode, title, maxCapacity));
            System.out.println("Course added successfully: " + courseCode + " - " + title);
        }
    }

    private void enrollStudent(Scanner scanner) {
        System.out.print("Enter student ID: ");
        String studentId = scanner.nextLine().trim();
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine().trim().toUpperCase();
        if (!students.containsKey(studentId)) {
            System.out.println("Error: Student with ID '" + studentId + "' not found.");
        } else if (!courses.containsKey(courseCode)) {
            System.out.println("Error: Course with code '" + courseCode + "' not found.");
        } else {
            students.get(studentId).enroll(courses.get(courseCode));
        }
    }

    private void dropStudent(Scanner scanner) {
        System.out.print("Enter student ID: ");
        String studentId = scanner.nextLine().trim();
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine().trim().toUpperCase();
        if (!students.containsKey(studentId)) {
            System.out.println("Error: Student with ID '" + studentId + "' not found.");
        } else if (!courses.containsKey(courseCode)) {
            System.out.println("Error: Course with code '" + courseCode + "' not found.");
        } else {
            students.get(studentId).drop(courses.get(courseCode));
        }
    }

    private void printStudents() {
        System.out.println("List of Students:");
        for (Student student : students.values()) {
            System.out.println(student);
        }
    }

    private void printCourses() {
        System.out.println("List of Courses:");
        for (Course course : courses.values()) {
            System.out.println(course);
        }
    }

    public static void main(String[] args) {
        UniversityDatabaseCLI universityDB = new UniversityDatabaseCLI();
        universityDB.run();
    }
}
