from django.shortcuts import render,get_object_or_404
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import Review
from .forms import BookAdminForm
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import  Book,Genre
from django.db.models.functions import Lower





# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def home(request):
    # Fetch the latest 5 books from the database
    latest_books = Book.objects.all().order_by('-id')[:34]  # assuming newer books have a higher ID
    return render(request, 'books/home.html', {'latest_books': latest_books})

def login_view(request):
    # Your login view logic here
    return render(request, 'books:home')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books:home')
    else:
        form = UserCreationForm()
    return render(request, 'books/signup.html', {'form': form})

def logout_view(request):
    # Your logout view logic here
    return render(request, 'books/logout.html')

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'An email has been sent with instructions to reset your password.')
            return redirect('books:password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'books/password_reset.html', {'form': form})

class CustomPasswordResetDoneView(PasswordResetDoneView):
    # Your custom password reset done view logic here
    template_name = 'books/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    # Your custom password reset confirm view logic here
    template_name = 'books/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    # Your custom password reset complete view logic here
    template_name = 'books/password_reset_complete.html'


def latest_reviews(request):
    # Get the latest 10 reviews
    latest_reviews = Review.objects.all().order_by('-date_posted')[:10]
    return render(request, 'books/latest_reviews.html', {'reviews': latest_reviews})

def top_rated(request):
    # Get the top 10 rated books
    top_rated_books = Book.objects.all().order_by('-average_rating')[:10]
    return render(request, 'books/top_rated.html', {'books': top_rated_books})




def community(request):
    # Example: Retrieve the latest 10 reviews or user posts for the community page
    latest_community_posts = Review.objects.all().order_by('-date_posted')[:10]

    # Pass the posts to the template
    return render(request, 'books/community.html', {'community_posts': latest_community_posts})

def about(request):
    # You can pass additional context if needed, such as team member information, etc.
    context = {
        'page_title': 'About Us'  # You can use this in your template to set the page title
    }
    return render(request, 'books/about.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookAdminForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            genre_name = form.cleaned_data['genre']
            try:
                genre = Genre.objects.get(name=genre_name)
                book.genre = genre
                book.save()
                return redirect('books:book_list')
            except Genre.DoesNotExist:
                messages.error(request, 'Invalid genre selected.')
        else:
            messages.error(request, 'Invalid form data. Please check the form fields.')
    else:
        form = BookAdminForm()

    return render(request, 'books/add_book.html', {'form': form})



def search_results(request):
    search_query = request.GET.get('search_query', '').strip()
    print("Search Query:", search_query)  # Add this line for debugging
    if search_query:
        # Use 'icontains' for case-insensitive partial matches in title or author
        books = Book.objects.filter(
            Q(title__icontains=search_query) | Q(author__icontains=search_query)
        )
        print("Books Found:", books)  # Add this line for debugging
    else:
        books = []

    return render(request, 'books/search_results.html', {'books': books})


@login_required
def submit_review(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            rating = data.get('rating')
            comment = data.get('comment')

            # Save the review data to your database (e.g., using a Django model)
            new_review = Review.objects.create(
                user=request.user,  # Assuming you have a 'user' field in your Review model
                rating=rating,
                comment=comment
            )

            response_data = {
                'success': True,
                'message': 'Review submitted successfully!',
                'comment': comment,
            }

            # Print the newly created review for debugging purposes
            print(f"New Review - Rating: {rating}, Comment: {comment}")

            return JsonResponse(response_data)
        except Exception as e:
            response_data = {
                'success': False,
                'message': 'Error while submitting the review.',
            }
            return JsonResponse(response_data, status=400)
        
def genre_books(request, genre_name):
    try:
        # Adjust the query to be case-insensitive
        genre = Genre.objects.get(name__iexact=genre_name.upper())
        books = Book.objects.filter(genre=genre)
    except Genre.DoesNotExist:
        genre = None
        books = []

    context = {
        'genre': genre,
        'books': books,
    }
    return render(request, 'books/genre_books.html', context)
