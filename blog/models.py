from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='blog_images')  
    sub_title = models.CharField(max_length=300)
    short_description = models.TextField()
    description = models.TextField()


    class Meta:
        db_table = "blogs"

    def __str__(self):
        return self.title
        
