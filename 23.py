import xml.etree.ElementTree as ET

root = ET.Element("Students")


def add_student(roll, name, branch, marks):
    student = ET.SubElement(root, "Student")

    ET.SubElement(student, "Roll").text = str(roll)
    ET.SubElement(student, "Name").text = name
    ET.SubElement(student, "Branch").text = branch
    ET.SubElement(student, "Marks").text = str(marks)


add_student(101, "Rahul", "CSE", 85)
add_student(102, "Aman", "ECE", 90)
add_student(103, "Priya", "CSE", 88)


def display_students():
    for student in root.findall("Student"):
        print("Roll:", student.find("Roll").text)
        print("Name:", student.find("Name").text)
        print("Branch:", student.find("Branch").text)
        print("Marks:", student.find("Marks").text)
        print("-------------------")


print("Student Information:")
display_students()

for student in root.findall("Student"):
    if student.find("Roll").text == "102":
        student.find("Name").text = "Aman Kumar"
        student.find("Marks").text = "95"

print("\nAfter Modification:")
display_students()

tree = ET.ElementTree(root)

# Apply indentation before saving (Python 3.9+)
ET.indent(tree, space="  ")

tree.write("students.xml", encoding="utf-8", xml_declaration=True)

print("XML file generated successfully.")=