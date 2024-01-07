from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import search_results



app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('home/', views.home, name='home'),  # Add this line
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),  # Add signup view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Add logout view
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Add password reset view
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('latest_reviews/', views.latest_reviews, name='latest_reviews'),
    path('top_rated/', views.top_rated, name='top_rated'),
    path('community/', views.community, name='community'),
    path('about/', views.about, name='about'),
    path('add/', views.add_book, name='add_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('search/', search_results, name='search_results'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('<str:genre_name>/', views.genre_books, name='genre_books'),

    
]
    

