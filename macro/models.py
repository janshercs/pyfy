from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogpost(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(db_index=True, auto_now_add=True)
    content = models.TextField()
    title = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.title

