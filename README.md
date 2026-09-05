# Library Book Manager

#### Video Demo: https://youtu.be/M93NOh_oicI?si=vCY-_CX_IzG1X8rK

#### Description:

Library Book Manager is a command-line Python application for managing a personal collection of books. The program allows users to add books, view all saved books, search for books, update their reading status, delete books, view reading statistics, and generate a library report.

The project stores book information in text files instead of using a database. This makes the application simple and easy to run while demonstrating Python concepts such as functions, lists, loops, conditionals, file handling, exception handling, and data validation.

## Features

### 1. Add a Book

Users can add a new book by entering:

* Book title
* Author
* Genre
* Publication year
* Reading status

The program validates the title, author, year, genre, and status before saving the book.

### 2. View All Books

Displays all saved books with their title, author, genre, publication year, and current reading status.

Books are displayed alphabetically by title.

### 3. Search Books

Users can search for books using a keyword. The program searches the book title, author, and genre and displays matching results.

### 4. Update Book Status

Users can select a book and change its reading status to:

* Available
* Reading
* Finished

### 5. Delete a Book

Users can select a book and delete it after confirming the deletion.

### 6. Reading Statistics

The program displays:

* Number of available books
* Number of books currently being read
* Number of finished books
* Total number of books
* Number of books in each genre

### 7. Generate Library Report

Users can generate a text report containing the current library information. They can generate a report for all books or filter the report by genre.

## Files

* `project.py` - Contains the main application and all library management features.
* `test_project.py` - Contains automated tests for important functions in the program.
* `DESIGN.md` - Explains the design decisions and structure of the project.
* `data/books.txt` - Stores book information.
* `data/genres.txt` - Stores the available genres.
* `reports/library_report.txt` - Stores the generated library report.

## How to Run

Make sure Python 3 is installed.

From the project directory, run:

```bash
python project.py
```

To run the automated tests:

```bash
pytest
```

The application automatically creates the required data and reports directories and initializes the necessary files when it starts.

## Design

The program is divided into several functions so that each function has a specific responsibility. File setup and data loading are separated from the main library features. This makes the code easier to understand and maintain.

Book information is stored as a list containing the title, author, genre, year, and status. The information is saved in a pipe-separated text file.

Input validation is used to prevent invalid years, genres, and statuses from being stored. The application also handles invalid menu choices and file-related errors.

The program uses a simple command-line menu so users can repeatedly perform different operations until they choose the Exit option.

## Testing

The project includes `test_project.py`, which tests genre loading, book loading, and saving/loading book data.

The test suite was run successfully with:

```text
3 passed
```
