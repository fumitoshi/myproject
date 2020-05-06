from django.shortcuts import render
from .models import Meal
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .forms import MealForm
from django.urls import reverse_lazy
import matplotlib.pyplot as plt
# Create your views here.
class MealListView(ListView):
    model=Meal
    template_name='kintore/meal_list.html'

    def queryset(self):
        return Meal.objects.all()

class MealCreateView(CreateView):
    model=Meal
    form_class=MealForm
    success_url=reverse_lazy('kintore:meallist')


def MealGraph(request):
    meal_data=Meal.objects.all()
    df=read_frame(meal_data,fieldnames=['date','weight','calorie','protein'])
    plt.hist(df)
    

        