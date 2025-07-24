from django.urls import path

from blog.views import index_Page,blogs_Page,blog_detail_Page

urlpatterns = [
    path("",index_Page),
    path("blogs/",blogs_Page),
    path("blog-detail/",blog_detail_Page)
]