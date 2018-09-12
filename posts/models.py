from django.db import models
from django.utils import timezone

# Create your models here.

# We'll create a new class called Post, and we'll base that on a standard model
class Post(models.Model):
    """
    A single blog post.
    When creating it, we need to think about what a blog post needs in order to
    come up with the necessary elements
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    # We want to see when our blog post was created so...
    created_date = models.DateTimeField(auto_now_add=True)
    # The attribute of (auto_now_add = true) means that as soon as a record is 
    # created, the current date and time will be added to that field.
    # Published date might be different to creation date, and we want to start
    # off with blank, allow null, and set the current time as default.
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    # We want to get the number of views, which starts at 0 by default
    views = models.IntegerField(default=0)
    # We want the user to be able to add tags so that we can group blog posts together
    tag = models.CharField(max_length=30, blank=True, null=True)
    # We want the user to be able to upload an image. Note "upload_to='img'" 
    # corresponds with the directory that we created under 'media'
    image = models.ImageField(upload_to='img', blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    