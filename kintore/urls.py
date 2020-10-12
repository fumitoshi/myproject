from django.urls import path
from . import views

app_name='kintore'

urlpatterns=[
  
    #path('meal_create/',views.MealCreateView.as_view(),name='meal_create'),
    #path('view_plot/',views.view_plot,name='view_plot'),
    
    #path('create_form/',views.MealCreateView.as_view(),name='create_form'),
    #path('detail/',views.project_detail_view,name='detail'),
    path('',views.KintoreFormView.as_view(),name='form_list'),
    path('update/<int:pk>/',views.MealUpdateView.as_view(),name='meal_update'),
    path('update_done/',views.update_done,name='update_done'),
    path('delete/<int:pk>/',views.MealDeleteView.as_view(),name='meal_delete'),
    path('delete_done/',views.delete_done,name='delete_done'),
]