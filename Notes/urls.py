from django.urls import path
from . import views

app_name = 'Notes'
urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),
   path('note/<int:pk>/', views.DetailView.as_view(), name='detail'),
   path('delete/<int:pk>/', views.DeleteNote.as_view(), name='delete'),
   path('update/<int:pk>', views.DeleteNote.as_view(), name='update') 
]