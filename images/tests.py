from django.test import TestCase
from .models import Image,Category,Location
import datetime as dt

# Create your tests here.

class ImageTestClass(TestCase):


  def setUp(self):

    self.name = Image(name='wildlife')
    

  def test_instance(self):
    self.assertTrue(isinstance(self.name, Image))

class CategoryTestClass(TestCase):

  def setUp(self):
    self.name = Category(name='techno')
    self.name.save()
    
  
  def test_instance(self):
    self.assertTrue(isinstance(self.name,Category))

  #test for delete
  def tearDown(self):
    self.name.delete()


class LocationTestClass(TestCase):
  def setUp(self):
    self.name = Location(name = 'nakuru')
    self.name.save()

  def test_instance(self):
    self.assertTrue(isinstance(self.name,Location))

  def test_updating_location(self):
     location = Location.get_location(self.nairobi)
     location.update_location('nairobi')
     location = Location.get_location(self.nairobi)
     self.assertTrue(location.location == 'nairobi')

  #test for deleting a location
