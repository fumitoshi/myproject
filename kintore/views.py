from django.shortcuts import render
from .models import Meal
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView,FormView,View
from .forms import MealForm
from django.urls import reverse_lazy
import matplotlib.pyplot as plt
from PIL import Image
from django_pandas.io import read_frame
from django.http import HttpResponse
import matplotlib.pyplot as plt
import io
from io import BytesIO
import plotly.graph_objs as go
from plotly.offline import plot
# Create your views here.


class KintoreFormView(FormView):
    template_name="kintore/meal_list.html"
    form_class=MealForm

    def form_valid(self,form):
        form.save()
        meal=Meal.objects.all().order_by("date")
        x=[data.date for data in meal]
        y=[data.weight for data in meal]
        y2=[data.calorie_intake for data in meal]
        y3=[data.bentipress for data in meal]
    

        trace0=go.Scatter(x=x,y=y,mode='lines',name='weight')
        trace1=go.Scatter(x=x,y=y2,mode='lines',name='calorie_intake')
        trace2=go.Scatter(x=x,y=y3,mode='lines',name='bentipress')

        layout=go.Layout(xaxis=dict(title='日付',type='date'),
                        yaxis=dict(title='体重'))

        fig=dict(data=[trace0,trace1,trace2],layout=layout)

        plot_html=plot(fig,output_type='div',include_plotlyjs=False)
        context={
            "form":self.form_class,
            "meal":Meal.objects.all(),
            "plot_html":plot_html,
        }
        df = read_frame(meal)
        df["link"] = df.id.apply(
            lambda x: f'<a href="/delete/{x}/">{x}</a>'
        )
        df = df.rename(columns={"id": "pk"})
        context["df"] = df.to_html(
            classes=["table", "table-bordered", "table-hover"],
            escape=False
        )

        return render(self.request,self.template_name,context)
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        meal=Meal.objects.all().order_by("date")
        # context["meal"]= Meal.objects.all().order_by("-date")[:5]
        df = read_frame(meal)
        print(df)
        df["link"] = df.id.apply(
            lambda x: f'<a href="/delete/{x}/">{x}</a>'
        )

        context["df"] = df.to_html(
            classes=["table", "table-bordered", "table-hover"],
            escape=False
        )
        
        context["meal"] = df.to_dict("records")
        x=[data.date for data in meal]
        y=[data.weight for data in meal]
        y2=[data.calorie_intake for data in meal]
        y3=[data.bentipress for data in meal]
    

        trace0=go.Scatter(x=x,y=y,mode='lines',name='weight')
        trace1=go.Scatter(x=x,y=y2,mode='lines',name='calorie_intake')
        trace2=go.Scatter(x=x,y=y3,mode='lines',name='bentipress')
        layout=go.Layout(xaxis=dict(title='日付',type='date'),
                        yaxis=dict(title='体重'))

        fig=dict(data=[trace0,trace1,trace2],layout=layout)

        plot_html=plot(fig,output_type='div',include_plotlyjs=False)
        context["plot_html"]=plot_html
        context["w"]=[data.weight for data in meal][-1]
        return context



class MealUpdateView(UpdateView):
    model=Meal
    form_class=MealForm
    success_url=reverse_lazy('kintore:update_done')

def update_done(request):
    return render(request,'kintore/update_done.html')

class MealDeleteView(DeleteView):
    model=Meal
    success_url=reverse_lazy('kintore:delete_done')

def delete_done(request):
    return render(request,'kintore/delete_done.html')






