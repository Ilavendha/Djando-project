# myapp/urls.py
from django.urls import path
from .views import create_study, study_list, delete_study

urlpatterns = [
    path('create_study/', create_study, name='create_study'),
     path('study_list/', study_list, name='study_list'), 
      path('delete/<int:pk>/', delete_study, name='delete_study'),

]



