from datetime import datetime
import os

# ======= FILE PATHS =======
BOOKS_FILE = "data/books.txt"
GENRES_FILE = "data/genres.txt"
REPORT_FILE = "reports/library_report.txt"

SEPARATOR = "|"


# ============================================
#  FILE SETUP
# ============================================

def setup_files():
    """Check if data files exist. If not, create them with defaults."""

    os.makedirs("data", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    try:
        open(GENRES_FILE, "r").close()
    except:
        file = open(GENRES_FILE, "w")
        file.write("Fiction\nNon-Fiction\nSci-Fi\nSelf-Help\nProgramming\nHistory\nBiography\nOther\n")
        file.close()

    try:
        open(BOOKS_FILE, "r").close()
    except:
        file = open(BOOKS_FILE, "w")
        file.write("Title|Author|Genre|Year|Status\n")
        file.close()


# ============================================
#  LOAD DATA FUNCTIONS
# ============================================

def load_genres():
    genres = []
    try:
        file = open(GENRES_FILE, "r")
        for line in file:
            line = line.strip()
            if line != "":
                genres.append(line)
        file.close()
    except:
        pass
    return genres


def load_all_books():
    books = []
    try:
        file = open(BOOKS_FILE, "r")
        lines = file.readlines()
        file.close()

        for line in lines[1:]:  # skip header
            parts = line.strip().split(SEPARATOR)
            if len(parts) == 5:
                books.append(parts)
    except:
        pass
    return books


# ============================================
#  HELPER FUNCTIONS
# ============================================

def display_menu():
    print("\n" + "=" * 50)
    print("       📚 LIBRARY BOOK MANAGER 📚")
    print("=" * 50)
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search Books")
    print("4. Update Book Status")
    print("5. Delete a Book")
    print("6. Reading Statistics")
    print("7. Generate Library Report")
    print("8. Exit")
    print("=" * 50)


def get_valid_genre(genres):
    print("\nAvailable Genres:")
    for i, genre in enumerate(genres, start=1):
        print(f"{i}. {genre}")

    while True:
        try:
            choice = int(input(f"Select genre (1-{len(genres)}): "))
            if 1 <= choice <= len(genres):
                return genres[choice - 1]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a valid number.")


def get_valid_year():
    current_year = datetime.now().year
    while True:
        try:
            year = int(input("Enter publication year: "))
            if 1000 <= year <= current_year:
                return str(year)
            else:
                print("Year must be between 1000 and current year.")
        except ValueError:
            print("Enter a valid year.")


def get_valid_status():
    statuses = ["Available", "Reading", "Finished"]
    print("\nBook Status:")
    for i, status in enumerate(statuses, start=1):
        print(f"{i}. {status}")

    while True:
        try:
            choice = int(input("Select status (1-3): "))
            if 1 <= choice <= 3:
                return statuses[choice - 1]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a valid number.")


def save_book(title, author, genre, year, status):
    try:
        file = open(BOOKS_FILE, "a")
        line = SEPARATOR.join([title, author, genre, year, status])
        file.write(line + "\n")
        file.close()
        print("✓ Book saved successfully!")
        return True
    except:
        print("Error saving book.")
        return False


def save_all_books(books):
    try:
        file = open(BOOKS_FILE, "w")
        file.write("Title|Author|Genre|Year|Status\n")
        for book in books:
            file.write(SEPARATOR.join(book) + "\n")
        file.close()
        return True
    except:
        print("Error saving books.")
        return False


# ============================================
#  MAIN FEATURES
# ============================================

def add_book():
    print("\n=== ADD A BOOK ===")
    genres = load_genres()
    if not genres:
        print("No genres available.")
        return

    title = input("Enter book title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    author = input("Enter author name: ").strip()
    if not author:
        print("Author cannot be empty.")
        return

    genre = get_valid_genre(genres)
    year = get_valid_year()
    status = get_valid_status()

    save_book(title, author, genre, year, status)


def view_all_books():
    print("\n=== ALL BOOKS ===")
    books = load_all_books()

    if not books:
        print("No books found!")
        return

    books.sort(key=lambda x: x[0].lower())

    for i, book in enumerate(books, start=1):
        print(f"\nBook #{i}")
        print(f"Title  : {book[0]}")
        print(f"Author : {book[1]}")
        print(f"Genre  : {book[2]}")
        print(f"Year   : {book[3]}")
        print(f"Status : {book[4]}")
        print("-" * 30)

    print(f"Total Books: {len(books)}")


def search_books():
    print("\n=== SEARCH BOOKS ===")
    books = load_all_books()

    if not books:
        print("No books found!")
        return

    keyword = input("Enter search keyword: ").strip().lower()
    if not keyword:
        print("Keyword cannot be empty.")
        return

    matches = []
    for book in books:
        if (keyword in book[0].lower() or
            keyword in book[1].lower() or
            keyword in book[2].lower()):
            matches.append(book)

    if not matches:
        print("No results found.")
    else:
        for book in matches:
            print(SEPARATOR.join(book))


def update_book_status():
    print("\n=== UPDATE BOOK STATUS ===")
    books = load_all_books()
    books.sort(key=lambda x: x[0].lower())

    if not books:
        print("No books found!")
        return

    view_all_books()

    try:
        choice = int(input("Select book number: "))
        if 1 <= choice <= len(books):
            new_status = get_valid_status()
            books[choice - 1][4] = new_status
            save_all_books(books)
            print("Status updated.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")


def delete_book():
    print("\n=== DELETE A BOOK ===")
    books = load_all_books()
    books.sort(key=lambda x: x[0].lower())

    if not books:
        print("No books found!")
        return

    view_all_books()

    try:
        choice = int(input("Select book number: "))
        if 1 <= choice <= len(books):
            confirm = input("Are you sure? (y/n): ").lower()
            if confirm == "y":
                books.pop(choice - 1)
                save_all_books(books)
                print("Book deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")


def reading_statistics():
    print("\n=== READING STATISTICS ===")
    books = load_all_books()

    if not books:
        print("No books found!")
        return

    available = reading = finished = 0

    for book in books:
        if book[4] == "Available":
            available += 1
        elif book[4] == "Reading":
            reading += 1
        elif book[4] == "Finished":
            finished += 1

    print(f"Available: {available}")
    print(f"Reading  : {reading}")
    print(f"Finished : {finished}")
    print(f"Total    : {len(books)}")

    genre_counts = {}
    for book in books:
        genre_counts[book[2]] = genre_counts.get(book[2], 0) + 1

    print("\nGenre Breakdown:")
    for genre, count in genre_counts.items():
        print(f"{genre}: {count}")


def generate_report():
    print("\n=== GENERATE LIBRARY REPORT ===")
    books = load_all_books()

    if not books:
        print("No books found!")
        return

    filter_choice = input("Enter genre to filter (or 'all'): ").strip()

    if filter_choice.lower() != "all":
        books = [b for b in books if b[2].lower() == filter_choice.lower()]

    report = "LIBRARY REPORT\n"
    report += "=" * 40 + "\n"
    report += f"Total Books: {len(books)}\n\n"

    for book in books:
        report += SEPARATOR.join(book) + "\n"

    try:
        file = open(REPORT_FILE, "w")
        file.write(report)
        file.close()
        print("Report generated successfully.")
    except:
        print("Error generating report.")


# ============================================
#  MAIN PROGRAM
# ============================================

def main():
    setup_files()
    print("\n🎉 Welcome to Library Book Manager!")

    while True:
        display_menu()

        choice = input("\n👉 Enter your choice (1-8): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_all_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            update_book_status()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            reading_statistics()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
