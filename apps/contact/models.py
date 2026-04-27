from django.db import models

class Contact(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=70,blank=True,unique=True)
    message= models.TextField(null=False, blank = False)
    
    def __str__(self):
        return self.title
    

    