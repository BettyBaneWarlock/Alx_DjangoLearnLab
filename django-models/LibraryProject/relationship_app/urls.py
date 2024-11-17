from django.urls import path
from .views import list_books, LibraryDetailView, UserLoginView, UserLogoutView, register

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
    path('login/', UserLoginView.as_view(), name='login'),  # Login URL
    path('logout/', UserLogoutView.as_view(), name='logout'),  # Logout URL
    path('register/', register, name='register'),  # Registration URL
]
