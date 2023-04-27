from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('shop/<int:pk>', views.ShopDetailView, name='shopDetail'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name='reviewDetail'),
    path('shop/create/', views.ShopCreateView.as_view(), name='shopCreate'),
    path('shop/<int:pk>/update/', views.ShopUpdateView.as_view(), name='shopUpdate'),
    path('shop/<int:pk>/delete/', views.ShopDeleteView.as_view(), name='shopDelete'),
    path('review/create/', views.ReviewCreateView.as_view(), name='reviewCreate'),
    path('review/<int:pk>/update/', views.ReviewUpdateView.as_view(), name='reviewUpdate'),
    path('review/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='reviewDelete'),
]