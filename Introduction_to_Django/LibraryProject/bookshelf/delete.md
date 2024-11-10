### Delete the Book Instance

from bookshelf.models import Book
retrieved_book.delete()
print(Book.objects.all())

### <QuerySet []>


