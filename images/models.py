from django.db import models
import datetime as dt

# Create your models here.



class Location(models.Model):
  name = models.CharField(max_length = 100)
  def __str__(self):
    
    return self.name


class Category(models.Model):
  name = models.CharField(max_length = 100)
  def __str__(self):
    return self.name


class Image(models.Model):
  name  = models.CharField(max_length = 30)
  description = models.TextField()
  location = models.ForeignKey(Location)
  category = models.ForeignKey(Category)
  image = models.ImageField(upload_to = 'images/')
  pub_date = models.DateField(auto_now_add=True)


  class Meta:
    ordering = ['name']


  @classmethod
  def get_all_images(cls):
    image =cls.objects.all()
    return image

  @classmethod
  def search_by_category(cls,category):
    gallery = cls.objects.filter(category__name__icontains=category)
    return gallery

  @classmethod
  def filter_by_location(cls,id):
    album = Image.objects.filter(location_id = id)

    return album


  def __str__(self):
    return self.name 

  def save_image(self):
    self.save()

  def update_image(self):
    self.update()
  
  def delete_image(self):
    self.delete()

  
  
