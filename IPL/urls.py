from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('problem1/', views.problem1, name="problem1"),
    path('problem1/graph', views.problem1_graph, name="problem1-output")
]
