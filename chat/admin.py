from django.contrib import admin
from chat.models import Messages, Friends
# Register your models here.

admin.site.register(Messages)
admin.site.register(Friends)