### Create a Book instance

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

### Expected Output
### <Book: 1984 by George Orwell (1949)>

### Retrieve the Book instance

retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

### Expected Output
### 1984 George Orwell 1949

### Update the Book Title

retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)

### Expected Output
### Nineteen Eighty-Four

### Delete the Book Instance

from bookshelf.models import Book
retrieved_book.delete()
print(Book.objects.all())

### Expected Output
### <QuerySet []>

