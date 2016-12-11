from __future__ import unicode_literals

from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=255) 
    content = models.TextField()
    udpated = models.DateTimeField(auto_now=True, auto_now_add=False)
    tiemstamp = models.DateTimeField(auto_now=False,auto_now_add=True)	

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

