from .import views
from django.urls import path

app_name ='projapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('tex',views.tex,name='tex'),

]
