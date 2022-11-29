from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(default=datetime.date.today)
    tags = models.TextField()
    image = models.ImageField(upload_to='images', blank=False, null=False)
    
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
    