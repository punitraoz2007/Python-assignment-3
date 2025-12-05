
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def menu():
    print("\n----- Library Inventory Manager -----")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                book = Book(title, author, isbn)
                inventory.add_book(book)
                print("Book added.")

            elif choice == "2":
                isbn = input("Enter ISBN: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.issue():
                    inventory.save_data()
                    print("Book issued.")
                else:
                    print("Cannot issue book.")

            elif choice == "3":
                isbn = input("Enter ISBN: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.return_book():
                    inventory.save_data()
                    print("Book returned.")
                else:
                    print("Cannot return book.")

            elif choice == "4":
                for b in inventory.display_all():
                    print(b)

            elif choice == "5":
                title = input("Enter title: ")
                results = inventory.search_by_title(title)
                for r in results:
                    print(r)

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
