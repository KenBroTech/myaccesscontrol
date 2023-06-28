from django.contrib import admin
from . models import CaesarEncrypt, cautionModel
# Register your models here.


class CaesarEncryptAdmin(admin.ModelAdmin):
    list_display = ('message', 'encrypted_message', 'key')


admin.site.register(CaesarEncrypt, CaesarEncryptAdmin)

class AESEncryptAdmin(admin.ModelAdmin):
    list_display = ('message', 'encrypted_message')


class cautionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')

admin.site.register(cautionModel, cautionModelAdmin)