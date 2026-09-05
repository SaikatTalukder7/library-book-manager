import project
from project import load_genres, load_all_books, save_all_books


def test_load_genres():
    genres = load_genres()
    assert len(genres) > 0
    assert "Fiction" in genres


def test_load_all_books():
    books = load_all_books()
    assert isinstance(books, list)


def test_save_all_books(tmp_path):
    books_file = tmp_path / "books.txt"

    books = [
        ["Test Book", "Test Author", "Fiction", "2024", "Finished"]
    ]

    original_file = project.BOOKS_FILE
    project.BOOKS_FILE = str(books_file)

    assert save_all_books(books) is True

    loaded_books = load_all_books()
    assert loaded_books == books

    project.BOOKS_FILE = original_file
