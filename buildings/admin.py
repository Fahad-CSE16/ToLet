from django.contrib import admin
from .models import FlatImages,Flat,District
class FlatInlines(admin.TabularInline):
    model=FlatImages
class FlatAdmin(admin.ModelAdmin):
    list_display=('user','rent','floor','district')
    inlines=[FlatInlines,]
# Register your models here.
admin.site.register(Flat,FlatAdmin)
admin.site.register(District)
