from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Create model for each blog post

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):

    categories = [
        ('Festivals', 'Festivals'),
        ('Clothing', 'Clothing'),
        ('Food', 'Food')
    ]
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=categories,
                                default='normal')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_articles')
    body = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    exerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    claps = models.ManyToManyField(User, related_name='blog_claps', blank=True)

    def get_absolute_url(self):
        return reverse('blog:single_post', args=[self.slug])

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_claps(self):
        return self.claps.count()


#  add comment section
class Comment(models.Model):
    user_name = models.CharField(max_length=80)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} written by {self.user_name}"
