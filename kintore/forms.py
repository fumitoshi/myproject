from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model=Meal
        fields=['date','weight','calorie_intake','protein','bentipress']