from django.shortcuts import render


posts = [
    {
        'author': 'Admin',
        'title': 'First post',
        'content': 'Sodejanie',
        'date_posted': '12/01/2023'
    },
    {
'author': 'User1',
        'title': 'Second post',
        'content': 'Sodejanie',
        'date_posted': '12/01/2023'
    }
]


def index(request):
    context = {
        'posts':posts
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html', {'title': '0 clube Python'})
# Create your views here.
