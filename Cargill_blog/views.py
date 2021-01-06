from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Meghana SM',
        'title': 'Docker and Kubernetes',
        'content': 'First post content',
        'date_posted': 'January, 2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

# Create your views here.
def Cargill_blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'Cargill_blog/Home.html', context)


def Cargill_about(request):
    return render(request, 'Cargill_blog/About.html', {'title': 'About'})