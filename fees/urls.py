from django.urls import path
from fees.views import FeeListView, FeeDetailView, FeeCreateView, FeeUpdateView, FeeDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(FeeListView.as_view()), name='fee.index'),
    path('<int:pk>/', login_required(FeeDetailView.as_view()), name='fee.detail'),
    path('create/', login_required(FeeCreateView.as_view()), name='fee.create'),
    path('<int:pk>/edit/', login_required(FeeUpdateView.as_view()), name='fee.update'),
    path('<int:pk>/delete/', login_required(FeeDeleteView.as_view()), name='fee.delete'),
]
