from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Tool(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

