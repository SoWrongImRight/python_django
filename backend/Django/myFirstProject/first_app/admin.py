from django.contrib import admin
from first_app.models import Topic, AccessRecords, Webpage

# Register your models here.
admin.site.register(AccessRecords)
admin.site.register(Webpage)
admin.site.register(Topic)