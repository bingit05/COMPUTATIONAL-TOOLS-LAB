class records:

    def __init__(self):

        self.students = []


    def insert_student(self):

        student = {

            "name" : input("enter the name of the student"),

            "Roll"  : int(input("enter your roll NO.")),

            "course" : input("Enter your course")
        }

        self.students.append(student)

        print("Student added Successfull\n")



    def delete_student(self):
        
        roll =  int(input("Enter the roll no. of the student"))

        for student in self.students:
            
            if(roll == student["Roll"]):

                self.students.remove(student)


        print("student not found")



    def search_student(self):
        
        roll =  int(input("Enter the roll no. of the student"))

        for student in self.students:

            if(roll == student["Roll"]):

                print("Name :", student["name"])

                print("Roll :", student["Roll"])

                print("Course ; ", student["course"])

                print("_____________________________")



obj = records()





while(True):

    print(" 1. Add Student")

    print(" 2. Delete Student")

    print(" 3. Search Student")

    n = int(input("Enter your choice"))

    if n == 1:
            
        obj.insert_student()

       
    elif n == 2:
            
            obj.delete_student()

    elif n == 3:
            
            obj.search_student()

    else:
            
        print("enter a valid choice")

        break