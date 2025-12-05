
import json
from pathlib import Path
from .book import Book
import logging

logging.basicConfig(level=logging.INFO, filename="library.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")

class LibraryInventory:
    def __init__(self, db_path="catalog.json"):
        self.db_path = Path(db_path)
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            if self.db_path.exists():
                data = json.loads(self.db_path.read_text())
                self.books = [Book(**item) for item in data]
                logging.info("Catalog loaded successfully.")
            else:
                self.books = []
        except Exception as e:
            logging.error(f"Error loading catalog: {e}")
            self.books = []

    def save_data(self):
        try:
            data = [b.to_dict() for b in self.books]
            self.db_path.write_text(json.dumps(data, indent=4))
            logging.info("Catalog saved.")
        except Exception as e:
            logging.error(f"Save failed: {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return self.books
