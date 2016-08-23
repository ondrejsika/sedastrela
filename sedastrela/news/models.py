from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    picture = models.ImageField(upload_to='sedastrela/news/news/picture', null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    short_description = models.TextField()
    long_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Gallery(models.Model):
    name = models.CharField(max_length=128)
    link = models.URLField()
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
