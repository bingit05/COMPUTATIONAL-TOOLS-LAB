class course:

    def __init__(self):

        self.java = set()
        self.python = set()


    def add_javastudent(self):

        name = input("Enter the name of the student")


        self.java.add(name)




    def add_pythonstudent(self):
        
        name = input("Enter the name of the student")

        self.python.add(name)

    

    def union_student(self):

        print("The students enrolled in atleast one courses are :\n")

        print(self.java.union(self.python))


    def intersection_student(self):

        print("The studenyt enrolled in both the courses are :")

        print(self.java.intersection(self.python))



    def only_python(self):

        print("The student enrolled in only python are :")

        print(self.python.difference(self.java))


    def only_java(self):

        print("The students enrolled in only java are:")

        print(self.java.difference(self.python))
        


obj = course()



while(True):


    print(" 1. add java student")
    print(" 2. Add python student")
    print(" 3. students in atleast one course")
    print(" 4. students enrolled in both courses")
    print(" 5. students enrolled only in python")
    print(" 6. students enrolled only in java")

    n = int(input("enter your choice"))


    if n == 1:

        obj.add_javastudent()


    elif n == 2:

        obj.add_pythonstudent()

    elif n == 3:

        obj.union_student()

    elif n ==  4:

        obj.intersection_student()

    elif n == 5:

        obj.only_python()

    elif n == 6:

        obj.only_java()

    else:


        print("enter  a valid choice")

        break




