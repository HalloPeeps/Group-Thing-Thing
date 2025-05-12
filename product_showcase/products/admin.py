from django.contrib import admin
from .models import Apple
from .models import LogMessage

# Register your models here.

admin.site.register(Apple) # allows admins to add more apple products to the database

@admin.register(LogMessage) # allows admins to view feedback from users
class LogMessageAdmin(admin.ModelAdmin):
    list_display = ('short_message', 'log_date')
    search_fields = ('message',)
    readonly_fields = ('message', 'log_date')

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    short_message.short_description = "Message"