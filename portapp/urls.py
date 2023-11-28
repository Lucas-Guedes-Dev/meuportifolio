from django.urls import path
from .views import Index, Contato

view_index = Index()
view_contrato = Contato()

urlpatterns = [
    path('', view_index.as_view, name='index'),
    path('contato', view_contrato.as_view, name='contato'),
]