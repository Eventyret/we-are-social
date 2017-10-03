from django.contrib import admin

# Register your models here.
from .models import Subject, Thread, Post

admin.site.register(Subject)
admin.site.register(Thread)
admin.site.register(Post)
