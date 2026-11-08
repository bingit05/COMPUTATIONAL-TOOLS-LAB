import xml.etree.ElementTree as ET
import pandas as pd


def parse_university_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # 1. Extract General University Info
    university_info = {
        "Name": root.attrib.get("name"),  #
        "Location": root.findtext("campus/location"),  #
        "Established": root.findtext("campus/established"),  #[cite: 1]
        "Website": root.findtext("campus/website"),  #[cite: 1]
    }

    students_data = []
    courses_data = []

    # 2. Iterate through Departments
    for dept in root.findall(".//department"):
        dept_id = dept.attrib.get("id")  #[cite: 1]
        dept_name = dept.findtext("name")  #[cite: 1]
        hod = dept.findtext("hod")  #[cite: 1]
        building = dept.findtext("building")  #[cite: 1]

        # 3. Iterate through Students in each Department
        for student in dept.findall(".//student"):
            student_id = student.attrib.get("id")  #[cite: 1]

            # Personal details
            p_details = student.find("personal_details")  #[cite: 1]
            first_name = p_details.findtext("name/first_name")  #[cite: 1]
            last_name = p_details.findtext("name/last_name")  #[cite: 1]
            full_name = f"{first_name} {last_name}"  #[cite: 1]
            gender = p_details.findtext("gender")  #[cite: 1]
            dob = p_details.findtext("date_of_birth")  #[cite: 1]
            phone = p_details.findtext("phone")  #[cite: 1]
            email = p_details.findtext("email")  #[cite: 1]

            # Address details
            address = p_details.find("address")  #[cite: 1]
            city = address.findtext("city")  #[cite: 1]
            state = address.findtext("state")  #[cite: 1]

            # Academic details
            a_details = student.find("academic_details")  #[cite: 1]
            year = a_details.findtext("year")  #[cite: 1]
            semester = a_details.findtext("semester")  #[cite: 1]
            cgpa = float(a_details.findtext("cgpa"))  #[cite: 1]
            advisor = a_details.findtext("advisor")  #[cite: 1]

            # Append flattened student object
            students_data.append(
                {
                    "Student ID": student_id,
                    "Name": full_name,
                    "Department ID": dept_id,
                    "Department Name": dept_name,
                    "Gender": gender,
                    "DOB": dob,
                    "Email": email,
                    "Phone": phone,
                    "City": city,
                    "State": state,
                    "Year": year,
                    "Semester": semester,
                    "CGPA": cgpa,
                    "Advisor": advisor,
                }
            )

            # 4. Iterate through Courses enrolled by the Student
            for course in a_details.findall(".//course"):
                courses_data.append(
                    {
                        "Student ID": student_id,
                        "Student Name": full_name,
                        "Course Code": course.attrib.get("code"),  #[cite: 1]
                        "Course Name": course.findtext("name"),  #[cite: 1]
                        "Credits": int(course.findtext("credits")),  #[cite: 1]
                        "Marks": int(course.findtext("marks")),  #[cite: 1]
                        "Grade": course.findtext("grade"),  #[cite: 1]
                    }
                )

    return university_info, pd.DataFrame(students_data), pd.DataFrame(courses_data)


# Execute parser
if __name__ == "__main__":
    uni_info, df_students, df_courses = parse_university_xml(
        "university_records.xml"
    )

    print("=== UNIVERSITY INFORMATION ===")
    for key, value in uni_info.items():
        print(f"{key}: {value}")

    print("\n=== STUDENTS DATA SUMMARY ===")
    print(df_students[["Student ID", "Name", "Department ID", "CGPA"]].to_string(index=False))

    print("\n=== SAMPLE COURSES DATA ===")
    print(df_courses.head(6).to_string(index=False))