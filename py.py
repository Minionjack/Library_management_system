class Library:
    def __init__(self):
        self.items = []
        self.members = []
        self.borrowings = []

    def add_item(self, item):
        self.items.append(item)

    def add_member(self, member):
        self.members.append(member)

    def add_borrowing(self, borrowing):
        self.borrowings.append(borrowing)

    def remove_item(self, item):
        self.items.remove(item)

    def remove_member(self, member):
        self.members.remove(member)

    def remove_borrowing(self, borrowing):
        self.borrowings.remove(borrowing)

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def get_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def add_item_menu(self):
        print("Add Item")
        item_id = input("Enter Item ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        publisher = input("Enter Publisher: ")
        year = input("Enter Year: ")

        print("Select Item Type:")
        print("1. Book")
        print("2. Article")
        print("3. Digital Media")
        item_type_choice = input("Enter your choice: ")

        if item_type_choice == "1":
            num_pages = input("Enter Number of Pages: ")
            language = input("Enter Language: ")
            item = Books(item_id, title, author, publisher, year, num_pages, language)
            self.add_item(item)
            print("Book added successfully.")
        elif item_type_choice == "2":
            journal_name = input("Enter Journal Name: ")
            issue_number = input("Enter Issue Number: ")
            item = Articles(item_id, title, author, publisher, year, journal_name, issue_number)
            self.add_item(item)
            print("Article added successfully.")
        elif item_type_choice == "3":
            file_format = input("Enter File Format: ")
            file_size = input("Enter File Size: ")
            item = DigitalMedia(item_id, title, author, publisher, year, file_format, file_size)
            self.add_item(item)
            print("Digital Media added successfully.")
        else:
            print("Invalid item type choice.")

    def remove_item_menu(self):
        print("Remove Item")
        item_id = input("Enter Item ID: ")
        item = self.get_item_by_id(item_id)
        if item:
            self.remove_item(item)
            print("Item removed successfully.")
        else:
            print("Item not found.")

    def add_member_menu(self):
        print("Add Member")
        member_id = input("Enter Member ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        member = Member(member_id, name, email, phone)
        self.add_member(member)
        print("Member added successfully.")

    def remove_member_menu(self):
        print("Remove Member")
        member_id = input("Enter Member ID: ")
        member = self.get_member_by_id(member_id)
        if member:
            self.remove_member(member)
            print("Member removed successfully.")
        else:
            print("Member not found.")

    def add_borrowing_menu(self):
        print("Add Borrowing")
        borrowing_id = input("Enter Borrowing ID: ")
        member_id = input("Enter Member ID: ")
        item_id = input("Enter Item ID: ")
        start_date = input("Enter Start Date: ")
        end_date = input("Enter End Date: ")

        member = self.get_member_by_id(member_id)
        item = self.get_item_by_id(item_id)

        if member and item:
            borrowing = Borrowing(borrowing_id, member, item, start_date, end_date)
            self.add_borrowing(borrowing)
            print("Borrowing added successfully.")
        else:
            print("Invalid member or item.")

    def remove_borrowing_menu(self):
        print("Remove Borrowing")
        borrowing_id = input("Enter Borrowing ID: ")
        for borrowing in self.borrowings:
            if borrowing.borrowing_id == borrowing_id:
                self.remove_borrowing(borrowing)
                print("Borrowing removed successfully.")
                return
        print("Borrowing not found.")

    def display_items(self):
        print("Items:")
        for item in self.items:
            print(item)

    def display_members(self):
        print("Members:")
        for member in self.members:
            print(member)

    def display_borrowings(self):
        print("Borrowings:")
        for borrowing in self.borrowings:
            print(borrowing)

class Items:
    def __init__(self, item_id, title, author, publisher, year):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"{self.item_id} | {self.title} | {self.author} | {self.publisher} | {self.year}"


class Books(Items):
    def __init__(self, item_id, title, author, publisher, year, num_pages, language):
        super().__init__(item_id, title, author, publisher, year)
        self.num_pages = num_pages
        self.language = language

    def __str__(self):
        return f"{super().__str__()} | {self.num_pages} | {self.language} | book"

class Articles(Items):
    def __init__(self, item_id, title, author, publisher, year, journal_name, issue_number):
        super().__init__(item_id, title, author, publisher, year)
        self.journal_name = journal_name
        self.issue_number = issue_number

    def __str__(self):
        return f"{super().__str__()} | {self.journal_name} | {self.issue_number} | article"


class DigitalMedia(Items):
    def __init__(self, item_id, title, author, publisher, year, file_format, file_size):
        super().__init__(item_id, title, author, publisher, year)
        self.file_format = file_format
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} | {self.file_format} | {self.file_size} | digital media"


class Member:
    def __init__(self, member_id, name, email, phone):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.member_id} | {self.name} | {self.email} | {self.phone}"


class Borrowing:
    def __init__(self, borrowing_id, member, item, start_date, end_date):
        self.borrowing_id = borrowing_id
        self.member = member
        self.item = item
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"{self.borrowing_id} | {self.member.member_id} | {self.item.item_id} | {self.start_date} | {self.end_date}"


# Create an instance of the library
library = Library()

# Load items
with open("items.txt", 'r') as f:
    for line in f:
        item_id, item_type, title, author, publisher, year, *args = line.strip().split("|")
        if item_type == "book":
            num_pages, language = args
            item = Books(item_id, title, author, publisher, year, num_pages, language)
        elif item_type == "article":
            journal_name, issue_number = args
            item = Articles(item_id, title, author, publisher, year, journal_name, issue_number)
        elif item_type == "digital_media":
            file_format, file_size = args
            item = DigitalMedia(item_id, title, author, publisher, year, file_format, file_size)
        else:
            print(f"Unknown item type: {item_type}")
            continue
        library.add_item(item)

# Load members
with open("members.txt") as f:
    for line in f:
        member_id, name, email, phone = line.strip().split("|")
        member = Member(member_id, name, email, phone)
        library.add_member(member)

# Load borrowing records
with open("borrowing.txt") as f:
    for line in f:
        borrow_id, member_id, item_id, borrow_date, return_date = line.strip().split("|")
        borrowing = Borrowing(borrow_id, library.get_member_by_id(member_id), library.get_item_by_id(item_id),
                              borrow_date, return_date)
        library.add_borrowing(borrowing)

# Run code
while True:
    print("\nLibrary Menu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Add Member")
    print("4. Remove Member")
    print("5. Add Borrowing")
    print("6. Remove Borrowing")
    print("7. Display Items")
    print("8. Display Members")
    print("9. Display Borrowings")
    print("0. Exit")

    choice = input("Enter your choice (0-9): ")


    if choice == "1":
        library.add_item_menu()
    elif choice == "2":
        library.remove_item_menu()
    elif choice == "3":
        library.add_member_menu()
    elif choice == "4":
        library.remove_member_menu()
    elif choice == "5":
        library.add_borrowing_menu()
    elif choice == "6":
        library.remove_borrowing_menu()
    elif choice == "7":
        library.display_items()
    elif choice == "8":
        library.display_members()
    elif choice == "9":
        library.display_borrowings()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")