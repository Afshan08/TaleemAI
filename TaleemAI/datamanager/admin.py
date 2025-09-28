from django.contrib import admin
from .models import UserProfile, Syllabus, MCQ

# Register your models here.
admin.site.register(UserProfile)
admin.site.site_header = "TaleemAI Admin"
admin.site.register(Syllabus)
admin.site.register(MCQ)
