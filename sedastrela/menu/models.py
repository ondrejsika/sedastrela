from django.db import models
from django.core.urlresolvers import reverse

from sedastrela.pages.models import Page


class Menu(models.Model):
    uid = models.CharField(max_length=32)
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return '%s - %s' % (self.uid, self.name)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items')
    label = models.CharField(max_length=32)
    link = models.CharField(max_length=256, null=True, blank=True)
    page = models.ForeignKey(Page, null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s - %s' % (self.menu, self.label)

    def get_link(self):
        if self.page:
            return reverse('sedastrela:pages:page', args=(self.page.id, self.page.slug))

        return self.link
