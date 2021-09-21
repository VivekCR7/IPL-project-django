from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('problem1/', views.problem1, name="problem1"),
    path('problem2/', views.problem2, name="problem2"),
    path('problem3/', views.problem3, name="problem3"),
    path('problem4/', views.problem4, name="problem4"),
    path('problem1/graph', views.problem1_graph, name="problem1-output"),
    path('problem2/graph', views.problem2_graph, name="problem2-output"),
    path('problem3/graph', views.problem3_graph, name="problem3-output"),
    path('problem4/graph', views.problem4_graph, name="problem4-output")
]
