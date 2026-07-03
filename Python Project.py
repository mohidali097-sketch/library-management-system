from abc import ABC, abstractmethod
from datetime import date, timedelta

class Book:
    def __init__(self, isbn, title, author, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

class Member(ABC):
    def __init__(self, member_id, name, contact):
        self.member_id = member_id
        self.name = name
        self.contact = contact
        self.borrowed_books = []

    @abstractmethod
    def get_borrow_limit(self):
        pass

class StudentMember(Member):
    def __init__(self, member_id, name, contact, department):
        Member.__init__(self, member_id, name, contact)
        self.department = department

    def get_borrow_limit(self):
        limit = 3
        return limit
    
class TeacherMember(Member):
    def __init__(self, member_id, name, contact, designation):
        Member.__init__(self, member_id, name, contact)
        self.designation = designation

    def get_borrow_limit(self):
        limit = 10
        return limit

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def addBook(self, isbn, title, author, total_copies):
        return Book(isbn, title, author, total_copies)

    def removeBook(self, title):
        found = False
        for book in L.books:
            if book.title == title:
                L.books.remove(book)
                found = True
                break
        if not(found):
            print("Book not found.")  

    def registerStudent(self, member_id, name, contact, department):
        return StudentMember(member_id, name, contact, department)
    
    def registerTeacher(self, member_id, name, contact, designation):
        return TeacherMember(member_id, name, contact, designation)
    
    def removeMember(self, member_id):
        found = False
        for member in L.members:
            if member.member_id == member_id:
                L.members.remove(member)
                found = True
                break
        if not(found):
            print("Member not found.")   

    def borrowBook(self, title, member_id):
        foundMember = False
        foundBook = False
        for member in L.members:
            if member.member_id == member_id:
                foundMember = True
                borrow_limit = member.get_borrow_limit()
                for book in L.books:
                    if book.title == title:
                        foundBook = True
                        if len(member.borrowed_books) < borrow_limit and book.available_copies > 0:
                            member.borrowed_books.append(book)
                            book.available_copies -= 1
                            transaction_id = int(input("Enter the transaction id: "))
                            T = Transaction(transaction_id, book, member)
                            L.transactions.append(T)
                            break
                        else:
                            if book.available_copies == 0:
                                print("No copies available.")
                            elif len(member.borrowed_books) >= borrow_limit:
                                print("Borrow limit reached.")
        if not(foundMember):
            print("Member not found.")
        if not(foundBook):
            print("Book not found.")

    def returnBook(self, title, member_id):
        foundMember = False
        foundBook = False
        foundTransaction = False     
        for member in L.members:
            if member.member_id == member_id:
                foundMember = True
                for book in member.borrowed_books:
                    if book.title == title:
                        foundBook = True
                        for transaction in L.transactions:
                            if transaction.member.member_id == member_id and transaction.book.title == title and transaction.return_date is None:
                                foundTransaction = True
                                fine = transaction.calculateFine()
                                transaction.fine = fine
                                book.available_copies += 1
                                member.borrowed_books.remove(book)
                                break
        if not(foundMember):
            print("Member not found.")
        if not(foundBook):
            print("Book not found.")
        if not(foundTransaction):
            print("Transaction not found.")       

    def displayBooks(self):
        for book in L.books:
            print("\nISBN: ", book.isbn)                             
            print("Title: ", book.title)
            print("Author: ", book.author)
            print("Total Copies: ", book.total_copies)
            print("Available Copies: ", book.available_copies)

    def searchBookByTitle(self, title):
        for book in L.books:
            if book.title == title:
                print("\nISBN: ", book.isbn)                             
                print("Title: ", book.title)
                print("Author: ", book.author)
                print("Total Copies: ", book.total_copies)
                print("Available Copies: ", book.available_copies)
                break

    def searchBookByAuthor(self, author):
        for book in L.books:
            if book.author == author:
                print("\nISBN: ", book.isbn)                             
                print("Title: ", book.title)
                print("Author: ", book.author)
                print("Total Copies: ", book.total_copies)
                print("Available Copies: ", book.available_copies)
                break   

    def displayBorrowedBooksOfMember(self, member_id):
        for member in L.members:
            if member.member_id == member_id:
                for book in member.borrowed_books:
                    print("\nISBN: ", book.isbn)                             
                    print("Title: ", book.title)
                    print("Author: ", book.author)
                    print("Total Copies: ", book.total_copies)
                    print("Available Copies: ", book.available_copies)

    def displayTransactionHistoryOfMember(self, member_id):
        for transaction in L.transactions:
            if transaction.member.member_id == member_id:
                print("\nTransaction ID: ", transaction.transaction_id)
                print("Book Title: ", transaction.book.title)
                print("Member ID: ", transaction.member.member_id)
                print("Borrow Date: ", transaction.borrow_date)
                print("Due Date: ", transaction.due_date)
                print("Return Date: ", transaction.return_date)
                print("Fine: ", transaction.fine)      

    def displayMembers(self):
        for member in L.members:
            if isinstance(member, StudentMember):
                print("\nMember ID: ", member.member_id)
                print("Name: ", member.name)
                print("Contact: ", member.contact)
                print("Department: ", member.department)
            elif isinstance(member, TeacherMember):
                print("\nMember ID: ", member.member_id)
                print("Name: ", member.name)
                print("Contact: ", member.contact)
                print("Designation: ", member.designation)                        

class Transaction:
    def __init__(self, transaction_id, book, member):  #transaction object will be created when book is borrowed
        self.transaction_id = transaction_id
        self.book = book
        self.member = member
        self.borrow_date = date.today()
        self.due_date = date.today() + timedelta(days = 14)
        self.return_date = None
        self.fine = 0

    def calculateFine(self):
        self.return_date = date.today()
        if self.return_date > self.due_date:
            days_late = (self.return_date - self.due_date).days
            if days_late >= 1 and days_late <= 3:
                self.fine = 200
            elif days_late >= 4 and days_late <= 7:
                self.fine = 500
            elif days_late >= 8 and days_late <= 14:
                self.fine = 1000
            elif days_late >= 15 and days_late <= 30:
                self.fine = 2000
            elif days_late > 30:
                self.fine = 5000
        else:
            print("Member is not fined as he returned the book within due date.")        

        return self.fine                                         

L = Library()

while True:

    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Register Member")
    print("4. Remove Member")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. View Books")
    print("8. Search Book")
    print("9. View a member's borrowed books")
    print("10. View a member's transaction history")
    print("11. View Members")
    print("12. Exit")

    choice = int(input("\nEnter the choice: "))

    while choice < 1 or choice > 12:
        print("Invalid choice. Try again.")
        choice = int(input("\nEnter the choice: "))
        if choice >= 1 and choice <= 12:
            break

    if choice == 1:
        isbn = int(input("Enter the isbn: "))
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        total_copies = int(input("Enter the total copies: "))
        L.books.append(L.addBook(isbn, title, author, total_copies))

    elif choice == 2:
        title = input("Enter the title of book to remove: ")
        L.removeBook(title)

    elif choice == 3:
        while True:
            print("\n1. Register Student")
            print("2. Register Teacher")
            print("3. Exit")

            subChoice = int(input("\nEnter the sub choice: "))

            while subChoice < 1 or subChoice > 3:
                print("Invalid sub choice. Try again.")
                subChoice = int(input("\nEnter the sub choice: "))
                if subChoice >= 1 and subChoice <= 3:
                    break 

            if subChoice == 1:
                member_id = int(input("Enter the member id: "))
                name = input("Enter the name: ")
                contact = input("Enter the contact: ")
                department = input("Enter the department: ")
                L.members.append(L.registerStudent(member_id, name, contact, department))

            elif subChoice == 2:
                member_id = int(input("Enter the member id: "))
                name = input("Enter the name: ")
                contact = input("Enter the contact: ")
                designation = input("Enter the designation: ")
                L.members.append(L.registerTeacher(member_id, name, contact, designation))

            elif subChoice == 3:
                break

    elif choice == 4:
        member_id = int(input("Enter the id of the member to remove: "))
        L.removeMember(member_id)

    elif choice == 5:
        title = input("Enter the title of book that is to be borrowed: ")
        member_id = int(input("Enter the id of the member who wants to borrow the book: "))
        L.borrowBook(title, member_id)            

    elif choice == 6:
        title = input("Enter the title of the book that is to be returned: ")
        member_id = int(input("Enter the id of the member who is returning the book: "))
        L.returnBook(title, member_id)

    elif choice == 7:
        L.displayBooks()

    elif choice == 8:
        while True:
            print("\n1. Search by title")
            print("2. Search by author")
            print("3. Exit")

            subChoice = int(input("\nEnter the sub choice: "))

            while subChoice < 1 or subChoice > 3:
                print("Invalid sub choice. Try again.")
                subChoice = int(input("\nEnter the sub choice: "))
                if subChoice >= 1 and subChoice <= 3:
                    break

            if subChoice == 1:
                title = input("\nEnter the title of book you want to search: ")
                L.searchBookByTitle(title)

            elif subChoice == 2:
                author = input("\nEnter the author of book you want to search: ")
                L.searchBookByAuthor(author)

            elif subChoice == 3:
                break    

    elif choice == 9:
        member_id = int(input("\nEnter the id of the member whose borrowed books you want to see: "))
        L.displayBorrowedBooksOfMember(member_id)

    elif choice == 10:
        member_id = int(input("\nEnter the id of the member whose transaction history you want to see: "))
        L.displayTransactionHistoryOfMember(member_id)

    elif choice == 11:
        L.displayMembers()

    elif choice == 12:
        break
