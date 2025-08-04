from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SingUpForm
from .models import Book , Genre ,Borrow
from django.contrib import messages

def homepage(request):
    home = "Welcome to the Library "
    genres = Genre.objects.all()
    return render(request , "homepage.html" , {"homepage":home , "genres":genres}  )

@login_required
def book_check(request):
    genre_id = request.GET.get("genre")
    genres = Genre.objects.all()
    
    if genre_id:
        books = Book.objects.filter(genre_id=genre_id)
    else:
        books = Book.objects.all()
    return render(request , "book_list.html" , {
        'books': books,
        'genres': genres,
        'selected_genre': int(genre_id) if genre_id else None
    })

@login_required
def borrow_book(request , book_id):
    book = get_object_or_404(Book , id = book_id)
    if book.available:
        Borrow.objects.create(user=request.user , book=book)
        book.available = False
        book.borrowed_by = request.user
        book.save()
    return redirect("book_check")
@login_required
def return_book(request , book_id):
    book = get_object_or_404(Book , id=book_id)
    borrow_record = Borrow.objects.filter( user=request.user , book_id=book_id , returned=False).first()
    if borrow_record:
        borrow_record.returned = True
        borrow_record.save()
        book.available = True
        book.save()
        messages.success(request , f"You returned '{book.name}' successfully ")
    else:
        messages.error(request , "Borrow record not found or already returned")
    return redirect("user_profile")


def singup(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("homepage")
    else:
        form = SingUpForm()
    return render(request , 'signup.html' , {'form':form})
@login_required
def user_profile(request):
    borrowed_books = Borrow.objects.filter(user=request.user , returned = False)
    return render(request , "profile.html" , {"borrowed_books":borrowed_books})

