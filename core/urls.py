from django.contrib import admin
from django.urls import path
from stocks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('stocks/', views.stock_list, name='stock_list'),  # GET/POST: List or create stock
    path('stocks/<int:stock_id>/', views.stock_detail, name='stock_detail'),  # GET/DELETE: Retrieve or delete stock
    path('stocks/<int:stock_id>/update/', views.stock_detail, name='stock_update'), # PUT: Update stock
]
