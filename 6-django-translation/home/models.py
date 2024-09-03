from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    content = models.TextField(verbose_name=_('Content'))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    facebook_id = models.URLField(verbose_name=_("Facebook Profile"), max_length=2048, null=True)

    class Meta:
        ordering= ('-created',)

    def __str__(self):
        return _(self.title)
