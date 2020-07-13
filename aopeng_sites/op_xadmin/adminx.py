import xadmin
from xadmin import views 
from op_xadmin.models import goods, ops, goodsInfo
	#, orderList, orderInfo, factoryInfo, deliveryInfo, deliveryList

# Register your models here.
class globalSetting(object):
	site_title = '奥鹏后台管理系统'
	site_footer = 'by zmz 2020.'
	menu_style = 'accordion'

xadmin.site.register(views.CommAdminView, globalSetting)

class BaseSetting(object):
	enable_themes = True
	use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)	

class goodsInfoInline():
	model = goodsInfo
	fields = ['color', 'size', 'normal_size_price', 'big_size_price']
	extra = 0

class goodsAdmin(object):
	list_display = ['op_id', 'kayouli_id', 'factory_name', 'goods_name']
	search_fields = ['op_id', 'kayouli_id', 'factory_name', 'goods_name']
	list_filter = ['op_id', 'kayouli_id', 'factory_name', 'goods_name']
	fields = ('kayouli_id', 'factory_name', 'goods_name')
	inlines = [goodsInfoInline]

xadmin.site.register(goods, goodsAdmin)

# class opsAdmin(object):
#     list_display = ['opera_name']
#
# xadmin.site.register(ops, opsAdmin)

class goodsInfoAdmin(object):
	list_display = ['op_id', 'color', 'size', 'normal_size_price', 'big_size_price']
	search_fields = ['op_id']
	list_filter = ['op_id']
	# list_display = ['factory_name', 'goods_name', 'color', 'size', 'normal_size_price', 'big_size_price']
	# search_fields = ['factory_name', 'goods_name']
	# list_filter = ['factory_name', 'goods_name']

xadmin.site.register(goodsInfo, goodsInfoAdmin)

# class factoryInfoAdmin(object):
# 	list_display = ['factory_id', 'factory_name']
# 	search_fields = ['factory_id', 'factory_name']
# 	list_filter = ['factory_id', 'factory_name']
#
# xadmin.site.register(factoryInfo, factoryInfoAdmin)
#
# class orderListAdmin(object):
# 	list_display = ['order_id', 'order_date']
# 	search_fields = ['order_id', 'order_date']
# 	list_filter = ['order_id', 'order_date']
#
# xadmin.site.register(orderList, orderListAdmin)
#
# class orderInfoAdmin(object):
# 	list_display = ['order_id', 'factory_name', 'goods_name', 'color', 'size', 'quantity']
# 	search_fields = ['factory_name', 'goods_name']
# 	list_filter = ['factory_name', 'goods_name']
#
# xadmin.site.register(orderInfo, orderInfoAdmin)

# class deliveryListAdmin(object):
# 	list_display = ['delivery_id', 'delivery_date', 'delivery_traceID']
# 	search_fields = ['delivery_date', 'delivery_traceID']
# 	list_filter = ['delivery_date', 'delivery_traceID']
#
# xadmin.site.register(deliveryList, deliveryListAdmin)
#
# class deliveryInfoAdmin(object):
# 	list_display = ['delivery_id', 'factory_name', 'goods_name', 'color', 'size', 'quantity']
# 	search_fields = ['factory_name', 'goods_name']
# 	list_filter = ['factory_name', 'goods_name']
#
# xadmin.site.register(deliveryInfo, deliveryInfoAdmin)
