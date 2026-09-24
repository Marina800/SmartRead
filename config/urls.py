from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.article_list, name='article_list'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)