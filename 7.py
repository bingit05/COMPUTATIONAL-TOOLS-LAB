class LibraryItem:
    def __init__(self,item_id,title):
        self.item_id = item_id
        self.title = title
        self.issued =  False 

    def display_details(self):
        pass

    def issue_item(self):

        if not self.issued:
            self.issued = True
            print(f"{self.title} has been issued ")

        else :
            print(f"{self.title} is already issued")

    def return_item(self):

        if self.issued:
            self.issued = False
            print(f"{self.title} has been returned")
        else:
            print(f"{self.title} was not issued ")


class Book(LibraryItem):
    def __init__(self,item_id,title,author):
        super().__init__(item_id,title)
        self.author = author

    def display_details(self):

        print("Book ID:",self.item_id)
        print("title:" ,self.title)
        print("Author:",self.author)
        print("status:", "issued" if self.issued else "Available")



class Megazine(LibraryItem):
    def __init__(self,item_id,title,issue_number):
        super().__init__(item_id,title)
        self.issue_number = issue_number

    def display_details(self):

        print("Megazine ID :",self.item_id)
        print("Title :",self.title)
        print("Issue Number :", self.issue_number)
        print("status:","issued" if self.issued else "Available")


class Journal(LibraryItem) :
    def __init__(self,item_id,title,research_field):
        super(). __init__(item_id,title)
        self.research_field = research_field

    def display_details(self):

        print("Journal ID: ",self.item_id)
        print("title:",self.title)
        print("research field",self.research_field)
        print("status:" ,"Issued" if self.issued else "Available")


items = [

    Book(101,"data structures", "badal soni"),
    Megazine(102,"programming","ripon patgiri"),
    Journal(103,"digital logic","samir")
]

print("=============LIBRARU ITEMS============")

for item in items:
    item.display_details()
    print()


print("=========ISSUES==========")

items[0].issue_item()
items[1].issue_item()
items[2].issue_item()


print("==========RETURN OPERATIONS===========")

items[0].return_item()
items[1].return_item()


print("\n=======UPDATED DETAILS =======")

for item in items:
    item.display_details()
    print()


