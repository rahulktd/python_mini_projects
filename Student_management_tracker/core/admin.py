from django.contrib import admin

from core.models import Students, Complaint, Reply, Notification

# Register your models here.
admin.site.register(Students),
admin.site.register(Complaint),
admin.site.register(Reply),
admin.site.register(Notification),
