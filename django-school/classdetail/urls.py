from django.urls import path
from classdetail.views import ClassDetailListView, ClassDetailView, ClassDetailCreateView, ClassDetailUpdateView, ClassDetailDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ClassDetailListView.as_view()), name='classdetail.index'),
    path('<int:pk>/', login_required(ClassDetailView.as_view()), name='classdetail.detail'),
    path('create/', login_required(ClassDetailCreateView.as_view()), name='classdetail.create'),
    path('<int:pk>/edit/', login_required(ClassDetailUpdateView.as_view()), name='classdetail.update'),
    path('<int:pk>/delete/', login_required(ClassDetailDeleteView.as_view()), name='classdetail.delete'),
]

