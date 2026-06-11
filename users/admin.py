from django.contrib import admin
from .models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display  = ('id', 'username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ('id', 'user', 'preview', 'created_at', 'updated_at')
    search_fields = ('text',)
    list_filter   = ('created_at',)

    def preview(self, obj):
        return obj.text[:60] + '...' if len(obj.text) > 60 else obj.text
    preview.short_description = 'Text Preview'
