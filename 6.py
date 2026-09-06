
input_file = "students.txt"
output_file = "results.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:

    outfile.write("RollNo\tName\tTotal\tAverage\tGrade\n")
    outfile.write("-" * 45 + "\n")

    for line in infile:
        data = line.strip().split()

        roll_no = data[0]
        name = data[1]
        marks = list(map(int, data[2:]))

        total = sum(marks)
        average = total / len(marks)

        # Determine grade
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        outfile.write(f"{roll_no}\t{name}\t{total}\t{average:.2f}\t{grade}\n")

print("Student results have been written to 'results.txt'.")