import sqlite3

# Connect to existing SQLite database
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()


# Generate department-wise employee salary report
def department_salary_report():
    department = input("Enter Department: ")

    # Parameterized SQL query
    query = """
        SELECT employee_id, name, designation, salary
        FROM employees
        WHERE department = ?
        ORDER BY salary DESC
    """

    cursor.execute(query, (department,))
    employees = cursor.fetchall()

    if not employees:
        print("\nNo employees found in this department.")
        return

    print("\n==============================================")
    print("       DEPARTMENT-WISE SALARY REPORT")
    print("==============================================")
    print("Department:", department)
    print("----------------------------------------------")

    print(f"{'ID':<10}{'Name':<20}"
          f"{'Designation':<22}{'Salary':>12}")

    print("-" * 64)

    total_salary = 0

    for employee in employees:
        employee_id, name, designation, salary = employee

        print(f"{employee_id:<10}"
              f"{name:<20}"
              f"{designation:<22}"
              f"{salary:>12.2f}")

        total_salary += salary

    average_salary = total_salary / len(employees)

    print("-" * 64)
    print(f"Number of Employees : {len(employees)}")
    print(f"Total Salary        : {total_salary:.2f}")
    print(f"Average Salary      : {average_salary:.2f}")


# Generate salary summary for all departments
def all_department_report():

    query = """
        SELECT department,
               COUNT(*) AS employee_count,
               SUM(salary) AS total_salary,
               AVG(salary) AS average_salary
        FROM employees
        GROUP BY department
        ORDER BY department
    """

    cursor.execute(query)
    departments = cursor.fetchall()

    if not departments:
        print("\nNo employee records found.")
        return

    print("\n==========================================================")
    print("             ALL DEPARTMENT SALARY REPORT")
    print("==========================================================")

    print(f"{'Department':<20}"
          f"{'Employees':<12}"
          f"{'Total Salary':<18}"
          f"{'Average Salary':<15}")

    print("-" * 65)

    for department in departments:
        name, count, total, average = department

        print(f"{name:<20}"
              f"{count:<12}"
              f"{total:<18.2f}"
              f"{average:<15.2f}")


# Main menu
def main():

    while True:
        print("\n==============================================")
        print("        EMPLOYEE SALARY REPORT SYSTEM")
        print("==============================================")
        print("1. Department-wise Employee Report")
        print("2. All Department Salary Summary")
        print("3. Exit")
        print("==============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            department_salary_report()

        elif choice == "2":
            all_department_report()

        elif choice == "3":
            print("Application closed.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start application
if __name__ == "__main__":
    try:
        main()
    finally:
        conn.close()