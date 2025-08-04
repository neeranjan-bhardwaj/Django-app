from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='name'),
    path('y/<int:id>', views.y, name='y'),
]