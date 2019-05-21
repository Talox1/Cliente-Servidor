from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Admin(models.Model):
    name = models.CharField(max_length=100, null=False)
    ap_pat = models.CharField(max_length=50, null=False)
    ap_mat = models.CharField(max_length=50, null=False)
    year = models.IntegerField(null=False)
    img = models.ImageField(upload_to='media/', null=True, blank=True)
    delete = models.BooleanField (default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table="Admin"

