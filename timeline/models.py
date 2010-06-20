from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=150)
    watched = models.DateField()
    location = models.ForeignKey('Location')
    
    def __unicode__(self):
        return self.name
    
    class Admin:
        pass

class Location(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=10, blank=True)
    lng = models.CharField(max_length=20, blank=True)
    lat = models.CharField(max_length=20, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Admin:
        pass
