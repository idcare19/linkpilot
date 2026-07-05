from django.db import models

# Create your models here.
class Link(models.Model):
    original_url = models.URLField(max_length=255)
    short_code = models.CharField(max_length=10, unique=True)
    custom_slug = models.CharField(max_length=50, blank=True, null=True)
    clicks = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
