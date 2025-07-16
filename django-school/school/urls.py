from django.urls import path
from school.views import SchoolListView, SchoolDetailView, SchoolCreateView, SchoolUpdateView, SchoolDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(SchoolListView.as_view()), name='school.index'),
    path('<int:pk>/', login_required(SchoolDetailView.as_view()), name='school.detail'),
    path('create/', login_required(SchoolCreateView.as_view()), name='school.create'),
    path('<int:pk>/edit/', login_required(SchoolUpdateView.as_view()), name='school.update'),
    path('<int:pk>/delete/', login_required(SchoolDeleteView.as_view()), name='school.delete'),
]