from django.contrib import admin
from .models import Task  # ✅ Register Task model

admin.site.register(Task)  # ✅ Ensure Task model appears in the Django Admin


# Register your models here.
