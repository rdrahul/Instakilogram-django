"""
Definition of models.
"""

from django.db import models
from django.core.urlresolvers import reverse
from gallery import ThumbnailImageField  
# Create your models here.

class Item(models.Model):
    """An Item is like an Album, it represent a set of photos"""
    name=models.CharField(max_length=150)
    description=models.TextField()
    
    class Meta:
        ordering=['name']
        
    def __str__(self):
         return self.name
    def __unicode__(self):
         return self.name
    
    def get_absolute_url(self):
        return reverse('item_detail',args=[self.id])
 
class Photo(models.Model):
     """ Model for an photo element"""
     item=models.ForeignKey('Item',on_delete=models.CASCADE)
     title=models.CharField(max_length=250)
     image=ThumbnailImageField(upload_to='photos')
     caption=models.CharField(max_length=250,blank=True)
     created=models.DateTimeField(auto_now=True)
     updated=models.DateTimeField(auto_now_add=True)
     
     class Meta:
         ordering=['title']
     
     def __str__(self):
         return self.title
     def __unicode__(self):
         return self.title
         
     def get_absolute_url(self):
         return reverse('photo_detail',args=[self.id])
    