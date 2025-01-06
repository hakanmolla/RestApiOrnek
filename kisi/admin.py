from django.contrib import admin
from .models import kisiler

# Register your models here.
# Register your models here.


@admin.register(kisiler)
class UrunlerAdmin(admin.ModelAdmin):
    list_display=('adi','soyadı','memleketi','ulkesi','tcno','olusturma_zamani','guncelleme_zamani')
    