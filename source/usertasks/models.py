from django.db import models
from company.models import Company 

class User(models.Model):
    name = models.CharField(max_length=45)
    company = models.ForeignKey(Company, related_name='users')
    username = models.CharField(max_length=20) 
    email = models.CharField(max_length=45)

    def __unicode__(self):
        return '%s: %s' % (self.username, self.email)

class Task(models.Model):
    title = models.CharField(max_length=45) 
    description = models.CharField(max_length=100)
    is_completed = models.BooleanField()
    user = models.ForeignKey(User)
