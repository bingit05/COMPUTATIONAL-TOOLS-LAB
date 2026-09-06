import sqlite3


conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    cgpa REAL NOT NULL,
    department TEXT NOT NULL
)
""")
conn.commit()


def add_student():
    try:
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        cgpa = float(input("Enter CGPA: "))
        department = input("Enter Department: ")

        cursor.execute("""
        INSERT INTO students (roll_no, name, cgpa, department)
        VALUES (?, ?, ?, ?)
        """, (roll_no, name, cgpa, department))

        conn.commit()
        print("Student added successfully.")

    except sqlite3.IntegrityError:
        print("Error: Roll number already exists.")
    except ValueError:
        print("Error: Enter valid numeric values for Roll No and CGPA.")


def display_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No student records found.")
        return

    print("\n------ Student Details ------")
    print(f"{'Roll No':<10}{'Name':<20}{'CGPA':<10}{'Department':<20}")
    print("-" * 60)

    for student in students:
        print(f"{student[0]:<10}{student[1]:<20}{student[2]:<10.2f}{student[3]:<20}")



def search_student():
    try:
        roll_no = int(input("Enter Roll No to search: "))

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        student = cursor.fetchone()

        if student:
            print("\nStudent Found")
            print("Roll No    :", student[0])
            print("Name       :", student[1])
            print("CGPA       :", student[2])
            print("Department :", student[3])
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter a valid Roll No.")



def update_student():
    try:
        roll_no = int(input("Enter Roll No to update: "))

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        name = input("Enter new Name: ")
        cgpa = float(input("Enter new CGPA: "))
        department = input("Enter new Department: ")

        cursor.execute("""
        UPDATE students
        SET name = ?, cgpa = ?, department = ?
        WHERE roll_no = ?
        """, (name, cgpa, department, roll_no))

        conn.commit()
        print("Student details updated successfully.")

    except ValueError:
        print("Please enter valid values.")



def delete_student():
    try:
        roll_no = int(input("Enter Roll No to delete: "))

        cursor.execute(
            "DELETE FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter a valid Roll No.")



def main():
    while True:
        print("\n========== Student Information Management System ==========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("===========================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please try again.")

    
    conn.close()



if __name__ == "__main__":
    main()
