from sqlite3 import connect

def create_database():
    conn = connect('FinalProject.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                        sid INTEGER PRIMARY KEY,
                        sname TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
                        cid INTEGER PRIMARY KEY,
                        cname TEXT,
                        credits INTEGER)''')  
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Enrolled (
                        sid INTEGER,
                        cid INTEGER,
                        FOREIGN KEY (sid) REFERENCES Students(sid),
                        FOREIGN KEY (cid) REFERENCES Courses(cid))''')
    
    conn.commit()
    conn.close()

def insert_data():
    conn = connect('FinalProject.db')
    cursor = conn.cursor()
    
    cursor.executemany('''INSERT OR IGNORE INTO Students (sid, sname) VALUES (?, ?)''', [
                        (1, 'Corey'),
                        (2, 'Shaun'),
                        (3, 'Michael'),
                        (4, 'KD'),
                        (5, 'Trent')])
    
    cursor.executemany('''INSERT OR IGNORE INTO Courses (cid, cname, credits) VALUES (?, ?, ?)''', [
                        (101, 'Math', 4),
                        (102, 'Science', 3),
                        (103, 'History', 3),
                        (104, 'English', 3),
                        (105, 'Coding', 4)])
    
    cursor.executemany('''INSERT OR IGNORE INTO Enrolled (sid, cid) VALUES (?, ?)''', [
                        (1, 101),
                        (1, 102),
                        (2, 103),
                        (3, 104),
                        (4, 105),
                        (5, 101),
                        (5, 102),
                        (5, 103),
                        (5, 104),
                        (5, 105)])
    
    conn.commit()
    conn.close()
    
def main_menu():
    print("\nStudent Menu:")
    print("L – List")
    print("E – Enroll")
    print("W – Withdraw")
    print("S – Search")
    print("M – My Classes")
    print("X – Exit")

def list_courses():
    conn = connect('FinalProject.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Courses")
    courses = cursor.fetchall()
    conn.close()
    print("\nCourses:")
    for course in courses:
        print(course)

def enroll_student():
    sid_input = input("\nEnter student ID (-1 to create a new student): ")
    if sid_input == '-1':
        create_new_student()
        return
    
    sid = int(sid_input)
    cid = int(input("Enter course ID: "))
    
    
    conn = connect('FinalProject.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE sid=?", (sid,))
    student = cursor.fetchone()
    cursor.execute("SELECT * FROM Courses WHERE cid=?", (cid,))
    course = cursor.fetchone()
    
    if student is None or course is None:
        print("Student or course does not exist.")
        return
    
  
    cursor.execute("SELECT * FROM Enrolled WHERE sid=? AND cid=?", (sid, cid))
    enrollment = cursor.fetchone()
    
    if enrollment:
        print("Student is already enrolled in this course.")
        return

    cursor.execute("INSERT INTO Enrolled (sid, cid) VALUES (?, ?)", (sid, cid))
    conn.commit()
    conn.close()
    print("Enrollment successful.")

def create_new_student():
    sname = input("Enter student name: ")
    sid = int(input("Enter student ID: "))
    
    conn = connect('FinalProject.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT sid FROM Students WHERE sid = ?", (sid,))
    existing_sid = cursor.fetchone()
    
    if existing_sid:
        print("Student ID already exists. Please choose a different ID.")
        conn.close()
        return
    
    cursor.execute("INSERT INTO Students (sid, sname) VALUES (?, ?)", (sid, sname))
    conn.commit()
    print("New student added successfully!")
    
    conn.close()
    
def withdraw_student():
    sid = int(input("\nEnter student ID: "))
    cid = int(input("Enter course ID: "))
     
    conn = connect('FinalProject.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Enrolled WHERE sid=? AND cid=?", (sid, cid))
    enrollment = cursor.fetchone()
    
    if enrollment is None:
        print("No such enrollment found.")
        return
    
    cursor.execute("DELETE FROM Enrolled WHERE sid=? AND cid=?", (sid, cid))
    conn.commit()
    conn.close()
    print("Withdrawal successful.")


def search_course():
    substring = input("\nEnter substring of course name: ")
    
    conn = connect('FinalProject.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Courses WHERE cname LIKE ?", ('%' + substring + '%',))
    courses = cursor.fetchall()
    conn.close()
    
    if courses:
        print("\nMatching courses:")
        for course in courses:
            print(course)
    else:
        print("No matching courses found.")

def my_classes():
    sid = int(input("\nEnter student ID: "))
    
    conn = connect('FinalProject.db')
    cursor = conn.cursor()
    cursor.execute("SELECT c.* FROM Courses c JOIN Enrolled e ON c.cid = e.cid WHERE e.sid=?", (sid,))
    courses = cursor.fetchall()
    conn.close()
    
    if courses:
        print("\nClasses enrolled by student:")
        for course in courses:
            print(course)
    else:
        print("No classes enrolled by this student.")

def menu_option(option):
    if option == 'L':
        list_courses()
    elif option == 'E':
        enroll_student()
    elif option == 'W':
        withdraw_student()
    elif option == 'S':
        search_course()
    elif option == 'M':
        my_classes()
    elif option == 'X':
        exit()
    else:
        print("Invalid option")

def run_application():
    create_database()
    insert_data()
    while True:
        main_menu()
        choice = input("Enter your choice: ").upper()
        menu_option(choice)

if __name__ == "__main__":
    run_application()   public static void main(String[] args) {
        UniversityDatabaseCLI universityDb = new UniversityDatabaseCLI();
        universityDb.run();
    }
}
