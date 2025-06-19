from django.urls import path
from .views import MaterialListView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView, MaterialDetailView

urlpatterns = [
    path('', MaterialListView.as_view(), name='material.index'),
    path('create/', MaterialCreateView.as_view(), name='material.create'),
    path('update/<int:pk>/', MaterialUpdateView.as_view(), name='material.update'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='material.delete'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='material.detail'),
]