from django.urls import  path
from op_xadmin import views

# app_name = 'op_xadmin'
#
urlpatterns = [
    path('/list', views.JSONResponse.goods_list),
	# path('<int:pk>/order_detail/', views.OrderDetailView.as_view(), name='order_detail'),
	]
