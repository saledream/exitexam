from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# class Student(models.Model):
#     studentId = models.CharField(max_length=255) 
#     studentName = models.CharField(max_length=255) 
#     email = models.CharField(max_length=255) 
#     department = models.CharField(max_length=255) 
#     picture = models.CharField(max_length=255) 
#     bio = models.CharField(max_length=255) 
#     year = models.CharField(max_field=255) 


# class Faculity(models.Model):
#     name = models.CharField(max_length=255)
     
# class Department(models.Model):
#     depName = models.CharField(max_length=255) 


# class Courses(models.Model):

#     title = models.CharField(max_length=255) 
#     description = models.CharField(max_length=255) 
#     abstract = models.CharField(max_length=255) 
#     image = models.CharField(max_length=255)
#     authorName = models.CharField(max_length=255) 

 
# class Instructors(models.Model):
#     email = models.CharField(max_length=255) 
#     name =  models.CharField(max_length=255)
#     picture = models.CharField(max_length=255)


# class Test(models.Model):
#     courseId = models.CharField(max_length=255)

class Subject(models.Model):

    title = models.CharField(max_length=255) 
    slug = models.SlugField(max_length=200, unique=True) 

    class Meta:
        ordering = ('title') 


    def __str__(self) -> str:
        return self.title 
    

class Course(models.Model):
    owner = models.ForeignKey(User, related_name='course_created') 

    subject = models.ForeignKey(Subject, 
                                on_delete=models.CASCADE,
                                  related_name="courses"
                                  )
    title = models.CharField(max_length=200) 
    slug = models.SlugField(max_length=200, unique=True) 
    overview = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ('-created') 

    
    def __str__(self):
        return self.title 
    

class Module(models.Model):
    course = models.ForeignKey(Course,related_name="modules") 
    title = models.CharField(max_length=200) 
    description = models.TextField(blank=True) 

    def __str__(self):

        return self.title 
    
