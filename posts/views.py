from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

# Create your views here.
# We're going to use three views... 

# The first one is going to be get_posts
def get_posts(request):
    """
    Create a view that returns a list of all the posts that were published
    prior to 'now' and renders them to a template called blogposts.html
    """
    # We start by creating a posts object and we'll filter them by published_date
    # We want them to be less than or equal to timezone now
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    # We'll now use the render library to return our blogposts.html template, which
    # is going to contain our list of posts
    return render(request, "blogposts.html", {'posts': posts})


# The second one will be the post_detail view...
def post_detail(request, pk):
    """
    This is going to return a single post object based on the post Id (pk)
    and render it to the post_detail.html template or return an error if 
    the post is not found 
    """
    # The get_object_or_404 is going to get our post item based on the post Id
    post = get_object_or_404(Post, pk=pk)
    # We'll also increment our views (so it adds 1 everytime we look at the detail
    # of it) and we'll save our post
    post.views += 1
    post.save()
    # This time we'll render our postdetail.html template, and again, we want to
    # send back out post object
    return render(request, "postdetail.html", {'post': post})
    

# The third one will be create_or_edit_post...
def create_or_edit_post(request, pk=None):
    """
    create a view that allows us to create or edit a post depending if the post
    is null or not
    """
    # Again, we create our post object
    post = get_object_or_404(Post, pk=pk) if pk else None
    
    if request.method == 'POST':
        # If the request method is post (this is the result of posting the form),
        # then we want to render our blog post form
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        #  If the form is valid, then we pass everything and save it
        if form.is_valid():
            post = form.save()
            # finally, we redirect back to our post detail form using our post Id
            return redirect(post_detail, post.pk)
    else:
        # if the request is not a POST
        form = BlogPostForm(instance=post)
        # We'll just return our blog post form with instance=post
    return render(request, 'blogpostform.html', {'form': form})