from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import gallery
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('gallery/', gallery, name='gallery'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# New lines below to serve static files in debug mode
import os
from django.urls import re_path
from django.views.static import serve


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': os.path.join(BASE_DIR, 'catalog/static'),
    }),
]