from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(blank=True, null=True, upload_to='images/%D/')

    def _str_(self):
        return self.title
