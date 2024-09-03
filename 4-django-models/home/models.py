from datetime import timedelta, datetime, date
from django.utils.timesince import timesince
from django.db import models
from django.utils import timezone
from .validators import validate_author_email
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save



# Create your models here.



PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)

class PostModelQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    
    def post_title_items(self, value):
        self.filter(title__icontains=value)

class PostModelManager(models.Manager):
    def get_queryset(self):
        return PostModelQuerySet(self.model, using=self._db)
    
    def all(self, *args, **kwargs):
        qs = super(PostModelManager, self).all(*args, **kwargs).active() #filter(active=True)
        # print(qs)
        return qs
    
    def time_frame(self, date1, date2):
        # assume datetime objects
        qs = self.get_queryset()
        qs_time_1 = qs.filter(publish_date__gte=date1)
        qs_time_2 = qs_time_1.filter(publish_date__lt=date2)
        # final_qs = (qs_time_1 | qs_time_2).distinct()
        return qs_time_2

class PostModel(models.Model):

    # ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    active          = models.BooleanField(default=True, verbose_name='Active Status')
    title           = models.CharField(
                        max_length=120, null=True, 
                        unique=True,
                        error_messages={
                        'unique': 'This title is not unique, please try again',
                        # 'blank' : 'This field is not full, please try again'
                        },
                        help_text='Must be a unique title'
                        )
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, default='draft', choices=PUBLISH_CHOICES)
    view_count      = models.IntegerField(default=0) 
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.CharField(max_length=240, null=True, blank=True, validators=[validate_author_email])
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects = PostModelManager()
    other = PostModelManager()

    @property
    def age(self):
        # return '{t} ago'.format(t=timesince(self.publish_date))
        if self.publish:
            now = datetime.now()
            publish_time = datetime.combine(
                            self.publish_date,
                            datetime.now().min.time()
            )

            try:
                difference = now - publish_time
            except:
                return 'Unknown'
            if difference <= timedelta(minutes=1):
                return 'Just now'
            return f'{timesince(publish_time).split(', ')[0]} ago'
        

    def save(self, *args, **kwargs):
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post' 
        verbose_name_plural = 'Posts'
        # unique_together = [('title', 'slug')]

    def __str__(self):
        return self.title
    
def post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print('Before save')
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)

pre_save.connect(post_model_pre_save_receiver, sender=PostModel)

def post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print('After save')
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(post_model_post_save_receiver, sender=PostModel)



