from django.shortcuts import render

# Create your views here.

# Add the following import
from django.http import HttpResponse
from .forms import WidgetsForm


# Define the home view


def index(request):
    widgets_form = WidgetsForm()
    return render(request, 'index.html')


def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save()
        new_widget.save()
    return redirect('index')


def widget_delete(reuqest, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('/')
