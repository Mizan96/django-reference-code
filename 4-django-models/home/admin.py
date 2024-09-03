from django.contrib import admin
from .models import PostModel

# Register your models here.
# @admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    # fields = '__all__'
    fields =   [
                'active',
                'title', 
                'slug', 
                'publish', 
                'content', 
                'publish_date', 
                'view_count',  
                'author_email',
                'updated',
                'timestamp',
                'new_content',
                'get_age',
                ]
    readonly_fields = ['updated', 'timestamp', 'new_content', 'get_age']

    def get_age(self, obj, *args, **kwargs):
        return str(obj.age)
    
    def new_content(self, obj, *args, **kwargs):
        return str(obj.title)
    # class Meta:
    #     model = PostModel
        

admin.site.register(PostModel, PostModelAdmin)