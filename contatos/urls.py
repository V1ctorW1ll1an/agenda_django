from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='<int:contato_id>', view=views.ver_contato, name='ver_contato')
]
