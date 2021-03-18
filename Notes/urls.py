from django.urls import path
from . import views

app_name = 'Notes'
urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),
   path('note/<int:pk>/', views.DetailView.as_view(), name='detail'),
   path('delete/<int:pk>/', views.DeleteNote.as_view(), name='delete'),
<<<<<<< HEAD
   path('update/<int:pk>/', views.UpdateNote.as_view(), name='update'),
   path('create', views.CreateNote.as_view(), name='create'),
  

]

=======
   path('update/<int:pk>', views.DeleteNote.as_view(), name='update') 
]
>>>>>>> 42e8d32d949e7cb54ac3f85d8b691c39c46f0da0
