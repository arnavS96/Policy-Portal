from django.contrib import admin

# Register your models here.
from .models import TeamModel, Member

admin.site.register(TeamModel)
admin.site.register(Member)

