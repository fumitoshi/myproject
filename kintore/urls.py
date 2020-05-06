from django.urls import path
from . import views

app_name='kintore'

urlpatterns=[
    path('',views.MealListView.as_view(),name='meallist'),
    path('meal_create/',views.MealCreateView.as_view(),name='meal_create'),
    path('meal_graph/',views.view_plot,name='view_plot'),
]