from django.urls import path
from . import views

urlpatterns = [
    path("" , views.homepage , name="homepage"),
    path("books/" , views.book_check , name="book_check"),
    path("borrow/<int:book_id>/" , views.borrow_book , name="borrow_book"),
    path("return/<int:book_id>/" , views.return_book , name="return_book"),
    path('profile/', views.user_profile, name='user_profile'),
    path("signup/" , views.signup , name="signup"),

]