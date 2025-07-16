from django.urls import path
from libraries.views import LibraryListView, LibraryDetailView, LibraryCreateView, LibraryUpdateView, LibraryDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(LibraryListView.as_view()), name='library.index'),
    path('<int:pk>/', login_required(LibraryDetailView.as_view()), name='library.detail'),
    path('create/', login_required(LibraryCreateView.as_view()), name='library.create'),
    path('<int:pk>/edit/', login_required(LibraryUpdateView.as_view()), name='library.update'),
    path('<int:pk>/delete/', login_required(LibraryDeleteView.as_view()), name='library.delete'),
]