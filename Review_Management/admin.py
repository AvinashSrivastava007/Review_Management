from django.contrib import admin

# Register your models here.
from Review_Management.models import ReviewMedia, Project, Department, SubmittedBy, ViewedBy

admin.site.register(ReviewMedia)
admin.site.register(Project)
admin.site.register(Department)
admin.site.register(SubmittedBy)
admin.site.register(ViewedBy)
