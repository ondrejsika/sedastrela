from django.db import models

from sedastrela.pages.models import Page


class Menu(models.Model):
    uid = models.CharField(max_length=32)
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu)
    label = models.CharField(max_length=32)
    link = models.URLField(null=True, blank=True)
    page = models.ForeignKey(Page, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s - %s' % (self.menu, self.name)
