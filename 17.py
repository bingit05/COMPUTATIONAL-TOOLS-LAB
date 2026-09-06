import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Create employee table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    designation TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")
conn.commit()


# CREATE - Add a new employee
def create_employee():
    try:
        employee_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        cursor.execute("""
        INSERT INTO employees
        (employee_id, name, designation, department, salary)
        VALUES (?, ?, ?, ?, ?)
        """, (employee_id, name, designation, department, salary))

        conn.commit()
        print("Employee added successfully.")

    except sqlite3.IntegrityError:
        print("Error: Employee ID already exists.")

    except ValueError:
        print("Error: Employee ID and Salary must be numeric.")


# READ - Display all employees
def read_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    if not employees:
        print("No employee records found.")
        return

    print("\n---------------- Employee Records ----------------")
    print(f"{'ID':<10}{'Name':<20}{'Designation':<20}"
          f"{'Department':<20}{'Salary':<12}")
    print("-" * 82)

    for employee in employees:
        print(f"{employee[0]:<10}"
              f"{employee[1]:<20}"
              f"{employee[2]:<20}"
              f"{employee[3]:<20}"
              f"{employee[4]:<12.2f}")


# READ - Search employee by ID
def search_employee():
    try:
        employee_id = int(input("Enter Employee ID to search: "))

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        employee = cursor.fetchone()

        if employee:
            print("\nEmployee Details")
            print("Employee ID :", employee[0])
            print("Name        :", employee[1])
            print("Designation :", employee[2])
            print("Department  :", employee[3])
            print("Salary      :", employee[4])
        else:
            print("Employee not found.")

    except ValueError:
        print("Please enter a valid Employee ID.")


# UPDATE - Update employee details
def update_employee():
    try:
        employee_id = int(input("Enter Employee ID to update: "))

        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        employee = cursor.fetchone()

        if not employee:
            print("Employee not found.")
            return

        print("\nEnter new employee details:")
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        cursor.execute("""
        UPDATE employees
        SET name = ?,
            designation = ?,
            department = ?,
            salary = ?
        WHERE employee_id = ?
        """, (name, designation, department, salary, employee_id))

        conn.commit()
        print("Employee updated successfully.")

    except ValueError:
        print("Please enter valid values.")


# DELETE - Delete an employee
def delete_employee():
    try:
        employee_id = int(input("Enter Employee ID to delete: "))

        cursor.execute(
            "DELETE FROM employees WHERE employee_id = ?",
            (employee_id,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    except ValueError:
        print("Please enter a valid Employee ID.")


# Main menu
def main():
    while True:
        print("\n==============================================")
        print("       EMPLOYEE MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. Create Employee")
        print("2. Read All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_employee()

        elif choice == "2":
            read_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("Exiting Employee Management System...")
            break

        else:
            print("Invalid choice. Please try again.")

    # Close database connection
    conn.close()


# Start the application
if __name__ == "__main__":
    main()
