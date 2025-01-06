from django.db import models

# Create your models here.

class kisiler(models.Model):
    adi=models.CharField(max_length=100)
    soyadı=models.CharField(max_length=100)
    memleketi=models.CharField(max_length=100)
    ulkesi=models.CharField(max_length=100)
    tcno=models.DecimalField(max_digits=11,decimal_places=0)
    olusturma_zamani=models.DateTimeField(auto_now_add=True)
    guncelleme_zamani=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.adi} {self.soyadı}"

