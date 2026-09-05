# Design Document: Library Book Manager

## Overview

Library Book Manager is a command-line application written in Python. It is designed to help a user manage a collection of books using a simple text-based menu.

The program focuses on keeping the application simple while demonstrating core Python programming concepts, including functions, lists, loops, conditional statements, file handling, exception handling, and input validation.

## Program Structure

The application is organized into several groups of functions.

### File Setup

The `setup_files()` function creates the required `data` and `reports` directories if they do not already exist. It also creates the genres and books files with default content when necessary.

This allows the program to start correctly even when the required files do not already exist.

### Loading Data

The `load_genres()` function reads the available genres from `data/genres.txt`.

The `load_all_books()` function reads book information from `data/books.txt`. Each book is stored as a list containing:

1. Title
2. Author
3. Genre
4. Year
5. Status

The first line of the books file is treated as a header and is skipped when loading the books.

### Input Validation

The program validates user input before saving information.

For example, `get_valid_year()` ensures that the publication year is between 1000 and the current year.

`get_valid_genre()` displays the available genres and ensures that the user selects a valid genre number.

`get_valid_status()` provides three valid reading statuses:

* Available
* Reading
* Finished

The program also checks that the book title and author are not empty.

### Saving Data

The `save_book()` function adds a new book to the books file.

The `save_all_books()` function rewrites the complete books file. It is used when a book is updated or deleted.

The pipe character (`|`) is used as a separator between fields.

For example:

```text
Title|Author|Genre|Year|Status
```

## Main Features

### Add a Book

The `add_book()` function collects the title, author, genre, publication year, and reading status from the user.

After validation, the book is saved to the books file.

### View All Books

The `view_all_books()` function loads all books and sorts them alphabetically by title.

Each book is displayed with its complete information and the total number of books is shown at the end.

### Search Books

The `search_books()` function allows the user to enter a keyword.

The keyword is searched against the title, author, and genre. The search is case-insensitive so that users do not have to match capitalization exactly.

### Update Book Status

The `update_book_status()` function displays the books and allows the user to select one.

The user can then choose a new reading status. The updated list is saved back to the books file.

### Delete a Book

The `delete_book()` function allows the user to select a book for deletion.

Before removing the book, the program asks the user for confirmation. If the user enters `y`, the selected book is removed and the updated list is saved.

### Reading Statistics

The `reading_statistics()` function counts books according to their reading status.

It displays the number of available, currently reading, and finished books. It also creates a genre breakdown by counting how many books belong to each genre.

### Generate Library Report

The `generate_report()` function creates a text report containing the books currently stored in the library.

The user can choose `all` to include every book or enter a genre to filter the report.

The generated report is saved as:

```text
reports/library_report.txt
```

## Testing

The project includes `test_project.py`.

The tests verify that:

* Genres can be loaded correctly.
* Books are loaded as a list.
* Books can be saved and loaded correctly.

The test suite was executed using:

```bash
pytest
```

All three tests passed successfully.

## Design Choices

The project uses text files rather than a database because the application is intended to be simple and easy to run. This also demonstrates Python file handling without requiring additional database software.

The program uses separate functions for different tasks so that each function has a clear responsibility. This makes the code easier to read, test, modify, and maintain.

A simple numbered menu was chosen because it provides an easy way for users to access all the available features from the command line.

## Future Improvements

Possible future improvements include:

* Adding book IDs for easier identification.
* Adding sorting by author, genre, or publication year.
* Adding more detailed reports.
* Adding a graphical user interface.
* Replacing text-file storage with a database for larger collections.
