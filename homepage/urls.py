from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('activedataentry/', views.ActiveDataEntry, name='activedataentry'),
    path('activedataentry/delete/', views.DeleteEntry, name='delete')
]