from django.contrib import admin
from django.utils.decorators import decorator_from_middleware_with_args
from .models import Pic,Comment
class PicAdmin(admin.ModelAdmin):
    exclude=('picture','type')
# Register your models here.
admin.site.register(Pic,PicAdmin)

admin.site.register(Comment)