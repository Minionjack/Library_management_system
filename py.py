class Library:
    def __init__(self):
        # Initialize a Library object with empty lists for items, members, and borrowings.
        self.items = []
        self.members = []
        self.borrowings = []

    def add_item(self, item):
        # Add an item to the library.
        self.items.append(item)

    def add_member(self, member):
        # Add a member to the library.
        self.members.append(member)

    def add_borrowing(self, borrowing):
        # Add a borrowing record to the library.
        self.borrowings.append(borrowing)

    def remove_item(self, item):
        # Remove an item from the library.
        self.items.remove(item)

    def remove_member(self, member):
        # Remove a member from the library.
        self.members.remove(member)

    def remove_borrowing(self, borrowing):
        # Remove a borrowing from the library
        self.borrowings.remove(borrowing)

    def get_item_by_id(self, item_id):
        # Find and return an item by its ID.
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def get_member_by_id(self, member_id):
        # Find and return a member by their ID.
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


    def write_items_to_file(self, file_name):
        with open(file_name, 'w') as f:
            for item in self.items:
                if isinstance(item, Books):
                    item_type = "book"
                    extra_info = f"{item.num_pages}|{item.language}"
                elif isinstance(item, Articles):
                    item_type = "article"
                    extra_info = f"{item.journal_name}|{item.issue_number}"
                elif isinstance(item, DigitalMedia):
                    item_type = "digital_media"
                    extra_info = f"{item.file_format}|{item.file_size}"
                else:
                    continue
                line = f"{item.item_id}|{item_type}|{item.title}|{item.author}|{item.publisher}|{item.year}|{extra_info}\n"
                f.write(line)

    def write_members_to_file(self, file_name):
        with open(file_name, 'w') as f:
            for member in self.members:
                line = f"{member.member_id}|{member.name}|{member.email}|{member.phone}\n"
                f.write(line)

    def write_borrowings_to_file(self, file_name):
        with open(file_name, 'w') as f:
            for borrowing in self.borrowings:
                line = f"{borrowing.borrowing_id}|{borrowing.member.member_id}|{borrowing.item.item_id}|{borrowing.start_date}|{borrowing.end_date}\n"
                f.write(line)

    def add_item_menu(self):
        # Display the menu for adding an item.
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
        # Display the menu for removing an item.
        print("Remove Item")
        item_id = input("Enter Item ID: ")
        item = self.get_item_by_id(item_id)
        if item:
            self.remove_item(item)
            print("Item removed successfully.")
        else:
            print('Item not found: ')

    def add_member_menu(self):
        # Display the menu for adding a member.
        print("Add Member")
        member_id = input("Enter Member ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        member = Member(member_id, name, email, phone)
        self.add_member(member)
        print("Member added successfully.")

    def remove_member_menu(self):
        # Display the menu for removing a member.
        print("Remove Member")
        member_id = input("Enter Member ID: ")
        member = self.get_member_by_id(member_id)
        if member:
            self.remove_member(member)
            print("Member removed successfully.")
        else:
            print("Member not found.")

    def add_borrowing_menu(self):
        # Display the menu for adding a borrowing record.
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
        # Display the menu for removing a borrowing record.
        print("Remove Borrowing")
        borrowing_id = input("Enter Borrowing ID: ")
        for borrowing in self.borrowings:
            if borrowing.borrowing_id == borrowing_id:
                self.remove_borrowing(borrowing)
                print("Borrowing removed successfully.")
                return
        print("Borrowing not found.")

    def display_items(self):
        # Display all items in the library.
        print("Items:")
        for item in self.items:
            print(item)

    def display_members(self):
        # Display all members in the library.
        print("Members:")
        for member in self.members:
            print(member)

    def display_borrowings(self):
        # Display all borrowing records in the library.
        print("Borrowings:")
        for borrowing in self.borrowings:
            print(borrowing)


class Items:
    def __init__(self, item_id, title, author, publisher, year):
        # Initialize an item with the provided attributes.
        self.item_id = item_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __str__(self):
        # Return a string representation of the item.
        return f"{self.item_id} | {self.title} | {self.author} | {self.publisher} | {self.year}"


class Books(Items):
    def __init__(self, item_id, title, author, publisher, year, num_pages, language):
        # Initialize a book with additional attributes for number of pages and language.
        super().__init__(item_id, title, author, publisher, year)
        self.num_pages = num_pages
        self.language = language

    def __str__(self):
        # Return a string representation of the book.
        return f"{super().__str__()} | {self.num_pages} | {self.language} | book"


class Articles(Items):
    def __init__(self, item_id, title, author, publisher, year, journal_name, issue_number):
        # Initialize an article with additional attributes for journal name and issue number.
        super().__init__(item_id, title, author, publisher, year)
        self.journal_name = journal_name
        self.issue_number = issue_number

    def __str__(self):
        # Return a string representation of the article.
        return f"{super().__str__()} | {self.journal_name}"

class DigitalMedia(Items):
    def __init__(self, item_id, title, author, publisher, year, file_format, file_size):
        # Initialize a digital media item with additional attributes for file format and file size.
        super().__init__(item_id, title, author, publisher, year)
        self.file_format = file_format
        self.file_size = file_size

    def __str__(self):
        # Return a string representation of the digital media item.
        return f"{super().__str__()} | {self.file_format} | {self.file_size} | digital media"

class Member:
    def __init__(self, member_id, name, email, phone):
        # Initialize a member with the provided attributes.
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        # Return a string representation of the member.
        return f"{self.member_id} | {self.name} | {self.email} | {self.phone}"

class Borrowing:
    def __init__(self, borrowing_id, member, item, start_date, end_date):
        # Initialize a borrowing record with the provided attributes.
        self.borrowing_id = borrowing_id
        self.member = member
        self.item = item
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        # Return a string representation of the borrowing record.
        return f"{self.borrowing_id} | {self.member.name} | {self.item.title} | {self.start_date} - {self.end_date}"

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
        library.write_items_to_file("items.txt")
    elif choice == "2":
        library.remove_item_menu()
        library.write_items_to_file("items.txt")
    elif choice == "3":
        library.add_member_menu()
        library.write_members_to_file("members.txt")
    elif choice == "4":
        library.remove_member_menu()
        library.write_members_to_file("members.txt")
    elif choice == "5":
        library.add_borrowing_menu()
        library.write_borrowings_to_file('borrowing.txt')
    elif choice == "6":
        library.remove_borrowing_menu()
        library.write_borrowings_to_file('borrowing.txt')
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
