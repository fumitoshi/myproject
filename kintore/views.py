from django.shortcuts import render
from .models import Meal
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from .forms import MealForm
from django.urls import reverse_lazy
import matplotlib.pyplot as plt
from PIL import Image
from django_pandas.io import read_frame
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

def view_plot(request):
    meal_data=Meal.objects.all()
    image=read_frame(meal_data,fieldnames=['date','weight','calorie_intake','protein'])
    plt.hist(image)
    response=HttpResponse(content_type="image/PNG")
    image.save(response,"PNG")
    return response







'''
class MealGraphView(TemplateView):
    template_name='kintore/graph.html'

    def view_plot(request):
        meal_data=Meal.objects.all()
        image=read_frame(meal_data,fieldnames=['date','weight','calorie','protein'])
        image=plt.hist(image)
        response=HttpResponse(content_type="image/png")
        image.save(response,"PNG")
        return response
'''
'''
    def MealGraph(request):
        meal_data=Meal.objects.all()
        image=read_frame(meal_data,fieldnames=['date','weight','calorie','protein'])
        response=HttpResponse(content_type="image/png")
        image.save(response,"PNG")
        return response
'''     

