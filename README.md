The Student Course Enrollment System
The Student Course Enrollment System is a command-line interface (CLI)-based application designed to manage student registrations, course enrollments, and withdrawals efficiently. By integrating with an SQLite database, the system ensures persistent and reliable storage of all student and course data, providing a streamlined experience for academic institutions.

This project showcases expertise in database design, SQL schema implementation, and backend development, making it a strong foundation for larger-scale student management systems.

Key Features
Student Management:

Allows users to add new students dynamically.
Prevents duplicate student IDs.
Course Catalog:

Maintains a list of available courses, including their name and credit hours.
Displays all courses stored in the database.
Enrollment System:

Allows students to enroll in courses.
Prevents duplicate enrollments.
Allows students to withdraw from courses if enrolled.
Search Functionality:

Enables users to search for courses by partial course name matching.
Personalized Course List:

Displays the list of courses a student is currently enrolled in.
Technical Implementation
Database Schema (SQLite)
Students Table (sid, sname) → Stores student details (Student ID and Name).
Courses Table (cid, cname, credits) → Stores course details (Course ID, Name, and Credits).
Enrolled Table (sid, cid) → Establishes a many-to-many relationship between students and courses.
Core Functionalities
Database Setup & Initialization

The system creates an SQLite database file (FinalProject.db) and defines tables for Students, Courses, and Enrollments.
It populates the database with sample data when initialized.
Command-Line Interface (CLI) Menu

Users interact with the system through a menu-driven interface with the following options:
L – List all courses
E – Enroll a student in a course
W – Withdraw a student from a course
S – Search for courses by name
M – Display all courses a student is enrolled in
X – Exit the application
Course Enrollment & Withdrawal

The system verifies whether a student and course exist before processing an enrollment request.
It checks if the student is already enrolled in the course to prevent duplicates.
Students can withdraw from courses they are currently enrolled in.
Dynamic Student Addition

Users can add new students if they do not already exist in the database.
The system ensures that student IDs are unique before inserting new students.
Search Functionality

Users can search for courses by entering a partial course name, retrieving all matching courses.
Student's Enrolled Course Lookup

Users can enter a student ID to retrieve and display all courses the student is enrolled in.
Data Integrity Enforcement

The system uses foreign keys to maintain relationships between tables and prevent invalid enrollments.
Project Significance
This system provides a structured and scalable approach to student course registration, leveraging SQLite for data persistence. It demonstrates strong SQL query design, relational database management, and Python-based backend development, making it an ideal foundation for university course management applications.
