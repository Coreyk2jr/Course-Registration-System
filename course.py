import java.sql.*;
import java.util.Scanner;

public class UniversityDatabaseCLI {
    private Connection connection;
    private Scanner scanner;

    public UniversityDatabaseCLI() {
        try {
            // Connect to the MySQL database
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/university_db", "root", "password");
            System.out.println("Connected to the database.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
        scanner = new Scanner(System.in);
    }

    public void run() {
        while (true) {
            printMenu();
            String choice = scanner.nextLine().trim();
            switch (choice) {
                case "1":
                    registerStudent();
                    break;
                case "2":
                    addCourse();
                    break;
                case "3":
                    enrollStudent();
                    break;
                case "4":
                    dropStudent();
                    break;
                case "5":
                    printStudents();
                    break;
                case "6":
                    printCourses();
                    break;
                case "7":
                    System.out.println("Exiting program. Goodbye!");
                    closeConnection();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please select a valid option.");
            }
        }
    }

    private void printMenu() {
        System.out.println("\nUniversity Database System Menu:");
        System.out.println("1. Register a new student");
        System.out.println("2. Add a new course");
        System.out.println("3. Enroll a student in a course");
        System.out.println("4. Drop a student from a course");
        System.out.println("5. Print all students");
        System.out.println("6. Print all courses");
        System.out.println("7. Exit");
    }

    private void registerStudent() {
        System.out.print("Enter student ID: ");
        String studentId = scanner.nextLine().trim();
        System.out.print("Enter student name: ");
        String name = scanner.nextLine().trim();

        try {
            PreparedStatement stmt = connection.prepareStatement("INSERT INTO students (student_id, name) VALUES (?, ?)");
            stmt.setString(1, studentId);
            stmt.setString(2, name);
            stmt.executeUpdate();
            System.out.println("Student registered successfully: " + name);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void addCourse() {
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine().trim().toUpperCase();
        System.out.print("Enter course title: ");
        String title = scanner.nextLine().trim();
        System.out.print("Enter maximum capacity: ");
        int maxCapacity = Integer.parseInt(scanner.nextLine().trim());

        try {
            PreparedStatement stmt = connection.prepareStatement("INSERT INTO courses (course_code, title, max_capacity) VALUES (?, ?, ?)");
            stmt.setString(1, courseCode);
            stmt.setString(2, title);
            stmt.setInt(3, maxCapacity);
            stmt.executeUpdate();
            System.out.println("Course added successfully: " + courseCode + " - " + title);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void enrollStudent() {
        System.out.print("Enter student ID: ");
        String studentId = scanner.nextLine().trim();
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine().trim().toUpperCase();

        // Add logic to enroll the student in the course using SQL queries
    }

    private void dropStudent() {
        System.out.print("Enter student ID: ");
        String studentId = scanner.nextLine().trim();
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine().trim().toUpperCase();

        // Add logic to drop the student from the course using SQL queries
    }

    private void printStudents() {
        try {
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM students");
            while (rs.next()) {
                System.out.println("Student ID: " + rs.getString("student_id") + ", Name: " + rs.getString("name"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void printCourses() {
        try {
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM courses");
            while (rs.next()) {
                System.out.println("Course Code: " + rs.getString("course_code") + ", Title: " + rs.getString("title") +
                        ", Capacity: " + rs.getInt("max_capacity"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private void closeConnection() {
        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        UniversityDatabaseCLI universityDb = new UniversityDatabaseCLI();
        universityDb.run();
    }
}
