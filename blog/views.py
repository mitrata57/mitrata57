from django.shortcuts import render
from blog.models import Blog
# Create your views here.
def index_Page(request):
    #Process Here
    return render(request,"index.html")

def blogs_Page(request):
    #Django ORM Feature
    blogs = Blog.objects.all()
    context = {
        "objects": blogs,
    }
    return render(request, "blogs.html",context)

def blog_detail_Page(request):
    return render(request,"blog-detail.html")

#MVT