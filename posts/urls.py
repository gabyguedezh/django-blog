from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post


# Once we've added the relevant imports, let's create our urlpatterns 

urlpatterns = [
    # The first one will be the root directory for the posts app
    url(r'^$', get_posts, name='get_posts'),
    # the next one will get the post_detail, for that, the regular expression
    # will allow us to get the id of a post
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    # The next one, is to be used if we want to create a new post. Note that in
    # in this case the name is different
    url(r'^new/$', create_or_edit_post, name='new_post'),
    # finally, if we want to edit, we'll also use the regular expression to
    # get the Id, but this time we'll add the word 'edit' to the url, and we'll
    # also include it in the name
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
    ]