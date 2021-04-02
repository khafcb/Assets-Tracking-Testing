  
from django.contrib import admin
from .models import Subscriber, Employee, RFID, Tag, Borrowing

# Register your models here.

admin.site.register(Subscriber)
admin.site.register(Employee)
admin.site.register(RFID)
admin.site.register(Tag)
admin.site.register(Borrowing)
