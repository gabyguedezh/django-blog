from django import forms
from .models import Post

# Note that we are importing the Post model we created in models.py, as we'll 
# use it to create our form

class BlogPostForm(forms.ModelForm):
    """
    We're gonna create a BlogPostForm using the Django forms library
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date')
        # Note that we don't have created_date nor views among the fields, 
        # because those are not user editable
        