from django.contrib import admin
from .models import ContactUs, Subscribers


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active', 'created_at', 'updated_at']
    list_display_links =['id', 'email']
    search_fields = ['email']
    list_filter = ['is_active']

admin.site.register(Subscribers, SubscribersAdmin)



class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'created_at', 'updated_at']
    list_display_links =['id', 'fullname']


admin.site.register(ContactUs, ContactUsAdmin)