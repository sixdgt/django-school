from django.urls import path
from results.views import ResultListView, ResultDetailView, ResultCreateView, ResultUpdateView, ResultDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ResultListView.as_view()), name='result.index'),
    path('<int:pk>/', login_required(ResultDetailView.as_view()), name='result.detail'),
    path('create/', login_required(ResultCreateView.as_view()), name='result.create'),
    path('<int:pk>/edit/', login_required(ResultUpdateView.as_view()), name='result.update'),
    path('<int:pk>/delete/', login_required(ResultDeleteView.as_view()), name='result.delete'),
]
