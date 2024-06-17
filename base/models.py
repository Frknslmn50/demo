from django.db import models

# Create your models here.

class Poem(models.Model):
    # By default, null is False, so we don't need to specify it
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)    
    content = models.TextField()
    author = models.CharField(max_length=50)
    # Auto now add will automatically add the date when the object is created
    created = models.DateTimeField(auto_now_add=True)
    # Auto now will automatically update the date when the object is updated
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title + ' by ' + self.author