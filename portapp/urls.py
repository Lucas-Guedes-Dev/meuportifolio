from django.urls import path
from .views import Index

view_index = Index()

urlpatterns = [
    path('', view_index.as_view, name='index'),
]