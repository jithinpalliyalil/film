from django.db import models


class movielist(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='pic')


    def __str__(self):
        return self.name

