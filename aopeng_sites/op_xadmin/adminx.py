import xadmin
from xadmin import views
import op_xadmin.xplugin
from op_xadmin.models import goods, ops
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

class goodsAdmin(object):
	list_display = ['op_id', 'kayouli_id', 'factory_name', 'goods_name']
	search_fields = ['op_id', 'kayouli_id', 'factory_name', 'goods_name']
	list_filter = ['op_id', 'kayouli_id', 'factory_name', 'goods_name']
	fields = ('kayouli_id', 'factory_name', 'goods_name', 'color', 'size', 'normal_size_price', 'big_size_price')
	custom_details = {'op_id': {'title': u'xx明细', 'load_url': 'detail2'}}

xadmin.site.register(goods, goodsAdmin)

# class opsAdmin(object):
#     list_display = ['opera_name']
#
# xadmin.site.register(ops, opsAdmin)

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
