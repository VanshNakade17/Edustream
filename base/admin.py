from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Classrooms)
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Assignments)
admin.site.register(Submissions)
admin.site.register(CustomUser)

from django.contrib import admin
from .models import Category, Video

from django.contrib import admin
from .models import Video, Category

# Register Category so that it can be managed via the admin
admin.site.register(Category)

# Register Video model with customization to display fields
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'duration', 'uploaded_at')
    search_fields = ('title', 'category__name')
    list_filter = ('category',)
    ordering = ('-uploaded_at',)
