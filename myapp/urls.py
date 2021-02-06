from django.urls import path
from . import views

urlpatterns = [
    path('view-book/', views.ViewBooks, name='view-book'),
    path('edit-book/<int:id>', views.EditBook, name='edit-book'),
    path('delete-book/<int:id>', views.DeleteBook, name='delete-book'),
    path('new-book/', views.NewBook, name='new-book'),
    path('search-book/', views.SearchBook, name='search-book'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogout, name='logout'),
]
