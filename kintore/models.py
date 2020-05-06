from django.db import models
from datetime import datetime
# Create your models here.
class Meal(models.Model):
    class Meta:
        db_table="meal"
        verbose_name="栄養"
        verbose_name_plural="栄養"
    
    date=models.DateField(verbose_name="日付",default=datetime.now)
    weight=models.IntegerField(verbose_name="体重",help_text="単位はkg")
    calorie_intake=models.IntegerField(verbose_name="カロリー",help_text="単位はkcal")
    protein=models.IntegerField(verbose_name="タンパク質",help_text="単位はg")

    def __str__(self):
        return self.date
