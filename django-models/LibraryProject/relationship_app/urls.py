from django.urls import path
from .views import list_books, LibraryDetailView, UserLoginView, UserLogoutView, register
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add/', views.add_book, name='add_book'),  # Path for adding a new book
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),  # Path for editing a specific book
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Path for deleting a specific book
]
