from django.shortcuts import render

def homepage(request):
    home = "Welcome to the Library "
    return render(request , "homepage.html" , {"homepage":home}  )
