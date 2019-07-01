from django.db import models

# Create your models here.

class Motor(models.Model):
    nama = models.CharField(max_length=100)
    thn_produksi = models.CharField(max_length=100)
    cc_motor = models.CharField(max_length=100)


    # def __init__(self):
    #     return self.nama