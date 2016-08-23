from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    picture = models.ImageField(upload_to='sedastrela/pages/page/picture', null=True, blank=True)
    page = models.TextField()
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.page


