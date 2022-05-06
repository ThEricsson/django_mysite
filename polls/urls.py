from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.post_list, name='posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('toteslesrespostes', views.totes, name='totes'),
]