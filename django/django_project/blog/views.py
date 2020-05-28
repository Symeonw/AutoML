from django.shortcuts import render

posts = [{
    "author: SymeonW",
    "title":"Blog Post 1",
    "content":"First post content",
    "date_posted": "May 26, 2020"
},
{
    "author: SymeonW",
    "title":"Blog Post 2",
    "content":"Second post content",
    "date_posted": "May 25, 2020"
}]

def home(request):
    context = {
        "posts":posts
    }
    return render(request, "blog/home.html", context)#accesses temples/blog/home.html

def about(request):
    return render(request, "blog/about.html")#accesses temples/blog/about.html