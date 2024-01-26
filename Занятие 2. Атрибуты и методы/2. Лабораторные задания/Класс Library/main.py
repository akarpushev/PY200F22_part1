from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages


# TODO написать класс Library
class Library:
    def __init__(self, books: Optional = None):
        self.books = []
        self.books = books
        #self.head = self.books[0]


    def get_next_book_id(self):
        if self.books:
            next_id = len(self.books) + 1
        else:
            next_id = 1
        return next_id


    def get_index_by_book_id(self, index):
        if self.books:
            for book in self.books:
                if book['id_'] == index:
                    return book.index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
