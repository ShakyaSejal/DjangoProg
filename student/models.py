from django.db import models

# Create your models here.
class Student(models.Model):
     name = models.TextField()
     course = models.TextField()

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save,post_save
from django.utils.text import slugify

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    course = models.TextField()
    slug = models.SlugField(unique = True, null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    publish = models.DateTimeField(auto_now_add = False, auto_now = True, null="True", blank = "True")
# blanks true or false
# save method
    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.name)
        super().save(*args,**kwargs)

def slugify_instance_title(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    qs = Student.objects.filter(slug=slug).order_by("-id")

    if qs.exists():
        new_slug = "%s-%s" %(slug, qs.first().id)
        return slugify_instance_title(instance, new_slug = new_slug)

def stu_pre_save(sender, instance, *args, **kwargs):
    print("pre_save")
    if instance.slug is None:
        instance.slug = slugify(instance.name)
pre_save.connect(stu_pre_save, sender=Student)

def stu_post_save(sender, instance, created, *args, **kwargs):
    print("post_save")
    print(args, kwargs)
    if created:
        instance.slug = slugify(instance.name)
        instance.save()
post_save.connect(stu_post_save, sender=Student)
# slugfield


