from django.contrib import admin

# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","name", "timestamp", "updated","publish","slug"]
    search_fields = ["name", "course","slug"]

admin.site.register(Student, StudentAdmin)

