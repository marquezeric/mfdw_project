from django.contrib import admin
from .models import Page

# Register your models here.
#  Creación de clase PageAdmin para cambiar la visualización del panel Admin
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Page, PageAdmin)