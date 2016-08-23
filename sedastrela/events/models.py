from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField()
    place = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='sedastrela/events/event/picture', null=True, blank=True)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()
    price = models.IntegerField()
    short_description = models.TextField()
    long_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


