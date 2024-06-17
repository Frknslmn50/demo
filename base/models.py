from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# One user can have many poems, but one poem can only have one user
class Poem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set default user ID here
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.title + ' by ' + self.author

# One poem can have many comments, but one comment can only have one poem
class Comment(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content