# Library Management System
A console-based Library Management System built in Python using Object-Oriented Programming concepts including abstract classes, inheritance, composition, and polymorphism.

---

## Classes

### `Book`
Represents a book in the library catalog.

| Attribute | Description |
|---|---|
| `isbn` | Unique identifier for the book |
| `title` | Title of the book |
| `author` | Author of the book |
| `total_copies` | Total copies owned by the library |
| `available_copies` | Copies currently available for borrowing |

---

### `Member` (Abstract)
Base class for all member types. Never instantiated directly.

| Attribute | Description |
|---|---|
| `member_id` | Unique identifier for the member |
| `name` | Name of the member |
| `contact` | Contact number |
| `borrowed_books` | List of currently borrowed books |

| Abstract Method | Description |
|---|---|
| `get_borrow_limit()` | Returns the borrow limit — defined by each subclass |

---

### `StudentMember(Member)`
Represents a student member.

| Extra Attribute | Description |
|---|---|
| `department` | Department the student belongs to |
| `get_borrow_limit()` | Returns 3 |

---

### `TeacherMember(Member)`
Represents a teacher member.

| Extra Attribute | Description |
|---|---|
| `designation` | Designation of the teacher e.g. Professor |
| `get_borrow_limit()` | Returns 10 |

---

### `Transaction`
Created every time a book is borrowed. Updated when the book is returned.

| Attribute | Description |
|---|---|
| `transaction_id` | Unique identifier for the transaction |
| `book` | Book object that was borrowed |
| `member` | Member object who borrowed it |
| `borrow_date` | Date the book was borrowed |
| `due_date` | Due date (borrow date + 14 days) |
| `return_date` | Date returned (None until returned) |
| `fine` | Fine amount (0 until overdue) |

| Method | Description |
|---|---|
| `calculateFine()` | Sets return date to today and calculates fine based on days late |

---

### `Library`
Main class that manages books, members, and transactions.

| Method | Description |
|---|---|
| `addBook()` | Creates and returns a new Book object |
| `removeBook()` | Removes a book from the catalog by title |
| `registerStudent()` | Creates and returns a new StudentMember object |
| `registerTeacher()` | Creates and returns a new TeacherMember object |
| `removeMember()` | Removes a member by member ID |
| `borrowBook()` | Handles book borrowing logic |
| `returnBook()` | Handles book return and fine calculation |
| `displayBooks()` | Displays all books in the catalog |
| `searchBookByTitle()` | Searches catalog by title |
| `searchBookByAuthor()` | Searches catalog by author |
| `displayBorrowedBooksOfMember()` | Shows currently borrowed books of a member |
| `displayTransactionHistoryOfMember()` | Shows full transaction history of a member |
| `displayMembers()` | Displays all registered members |

---

## Fine Structure

| Days Late | Fine (Rs.) |
|---|---|
| 1 - 3 days | 200 |
| 4 - 7 days | 500 |
| 8 - 14 days | 1000 |
| 15 - 30 days | 2000 |
| 30+ days | 5000 |

---

## Features

- Add and remove books from the catalog
- Register and remove student and teacher members
- Borrow a book with limit and availability checks
- Return a book with automatic fine calculation
- View all books in the catalog
- Search books by title or author
- View a member's currently borrowed books
- View a member's full transaction history
- View all registered members

---

## OOP Concepts Used

| Concept | Where Used |
|---|---|
| Abstract Class | `Member` — cannot be instantiated directly |
| Inheritance | `StudentMember` and `TeacherMember` inherit from `Member` |
| Polymorphism | `get_borrow_limit()` behaves differently per member type |
| Composition | `Library` is composed of lists of `Book`, `Member`, and `Transaction` objects |
| Encapsulation | Each class manages its own data and behavior |

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python library.py
```

---

## Menu Options

```
1.  Add Book
2.  Remove Book
3.  Register Member
4.  Remove Member
5.  Borrow Book
6.  Return Book
7.  View Books
8.  Search Book
9.  View a member's borrowed books
10. View a member's transaction history
11. View Members
12. Exit
```
