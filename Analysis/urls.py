from django.urls import path
from .views import Scatter, GetAttributes, BarPlot, PieChart

urlpatterns = [
    path('attributes/', GetAttributes.as_view(), name='get_attributes'), 
    path('scatter/', Scatter.as_view(), name='scatter'), 
    path('bar/', BarPlot.as_view(), name='bar_plot'), 
    path('pie/', PieChart.as_view(), name='pie_chart'), 
]