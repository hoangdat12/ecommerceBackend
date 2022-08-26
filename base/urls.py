from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import deleteProduct, getProduct, getProducts, createProduct, deleteProduct, getProductCategory, getCategory, MyTokenObtainPairView

urlpatterns = [
    path('product/getProduct/<int:pk>', getProduct),
    path('product/getProducts', getProducts),
    path('product/create', createProduct),
    path('product/delete/<int:pk>', deleteProduct),
    path('category/get', getCategory),
    path('category/allproduct/<int:pk>', getProductCategory),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]