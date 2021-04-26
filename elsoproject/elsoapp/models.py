from django.db import models

# Create your models here.
class Arucikk(models.Model):
    nev = models.CharField(max_length=128, default='')
    db = models.IntegerField(default=0)
    mertekegyseg = models.CharField(max_length=128, default='')

    class Meta:
        verbose_name = 'Áru'
        verbose_name_plural = 'Áruk'

    def __str__(self):
        return f"{self.db}{self.mertekegyseg} {self.nev}"

    def hozzaadas(post):
        Arucikk.objects.create(nev=post['Árucikk_neve'], db=post['dbszam'], mertekegyseg=post['mértékegység'])

    def eltuntetes(post):
        for i in Arucikk.objects.all():
            for key in post.keys():
                if key==str(i):
                    i.delete()
                    
                

