from django.contrib import admin

# Register your models here.

from .models import Link
 
class LinkAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'clicks', 'is_active', 'created_at')
    search_fields = ('original_url', 'short_code', 'custom_slug')
    
admin.site.register(Link, LinkAdmin)