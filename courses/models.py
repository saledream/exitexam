from django.db import models
from django.contrib.auth.models import User 
from .fields import OrderField  
# Create your models here.

class Subject(models.Model):

    title = models.CharField(max_length=255) 
    slug = models.SlugField(max_length=200, unique=True) 

    class Meta:
        ordering = ('title',) 


    def __str__(self) -> str:
        return self.title 
    

class Course(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_created') 

    subject = models.ForeignKey(Subject, 
                                on_delete=models.CASCADE,
                                  related_name="courses"
                                  )
    title = models.CharField(max_length=200) 
    slug = models.SlugField(max_length=200, unique=True) 
    overview = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ('-created',) 

    
    def __str__(self):
        return self.title 
    

class Module(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE, related_name="modules") 
    title = models.CharField(max_length=200) 
    description = models.TextField(blank=True) 
    order = OrderField(blank=True,for_fields=['course']) 

    def __str__(self):

        return '{}.{}'.format(self.order,self.title) 
    

from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey 

class Content(models.Model):
    module = models.ForeignKey(Module, 
                               on_delete=models.CASCADE,
                               related_name="contents",
                               limit_choices_to= {
                                   'model__in': ('text','image')
                               },
                               )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) 
    object_id = models.PositiveIntegerField() 
    item = GenericForeignKey('content_type','object_id') 
    order = OrderField(blank=True,for_fields=['content']) 

    class Meta:
        ordering = ['order'] 

    

class ItemContent(models.Model):

    title = models.CharField(max_length=255) 
    created = models.DateTimeField(auto_now_add=True) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="%(class)s_related")
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 

    class Meta:
        abstract = True 

    def __str__(self) -> str:
        return self.title 
    

    

class Text(ItemContent):
    body = models.TextField() 

class Image(ItemContent):
    file = models.ImageField(upload_to='images')



