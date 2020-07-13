from django.db import models

# Create your models here.
class ops(models.Model): 
	opera_name = models.CharField(max_length=32, unique=True, verbose_name=u"管理员名称")  
	opera_age = models.CharField(max_length=32, default = '23', verbose_name=u"管理员年龄")  

	class Meta: 
		db_table = 'ops' 
		verbose_name = '管理员信息表' 
		verbose_name_plural = verbose_name 

	def __str__(self): 
		return self.opera_name
		
class goods(models.Model):
	op_id = models.CharField(primary_key=True, max_length=15, unique=True, verbose_name=u"奥鹏编号")
	kayouli_id = models.CharField(max_length=32, blank=True, null=True,default=None, verbose_name=u"卡友立货号")
	factory_name = models.CharField(max_length=32, blank=True, null=True,default=None, verbose_name=u"工厂名")
	goods_name = models.CharField(max_length=32, blank=True, null=True,default=None, verbose_name=u'货号')
	
	class Meta:
		db_table = 'goodsList'
		verbose_name = '产品列表'
		verbose_name_plural = verbose_name

	def __str__(self):
		return '%s&%s' % (self.factory_name, self.goods_name)


class goodsInfo(models.Model):
	op_id = models.ForeignKey('goods', on_delete=models.CASCADE, primary_key=True)
	color = models.CharField(max_length=100, default=None, null=False, blank=False, verbose_name=u'颜色')
	size = models.CharField(max_length=100, default=None, null=False, blank=False, verbose_name=u'尺码')
	normal_size_price = models.PositiveIntegerField(verbose_name=u'普码价格')
	big_size_price = models.PositiveIntegerField(verbose_name=u'大码价格')

	class Meta:
		db_table = 'goodsDetails'
		verbose_name = '产品详细信息'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.op_id

# class factoryInfo(models.Model):
# 	factory_id = models.CharField(max_length=5, unique=True, default=None, null=False, blank=False)
# 	factory_name = models.CharField(max_length=32, unique=False, default=None, null=False, blank=False)
#
# 	class Meta:
# 		db_table = 'factoryInfo'
# 		verbose_name = '工厂信息'
# 		verbose_name_plural = verbose_name
#
# 	def __str__(self):
# 		return self.factory_id

# class orderList(models.Model):
# 	order_id = models.AutoField(primary_key=True, verbose_name=u'订单编号')
# 	order_date = models.DateField(verbose_name=u'订单日期')
#
# 	class Meta:
# 		db_table = 'orderList'
# 		verbose_name = '订单列表'
# 		verbose_name_plural = verbose_name
#
# 	def __str__(self):
# 		return self.order_id
#
# class orderInfo(models.Model):
# 	order_id = models.ForeignKey("orderList", on_delete=models.CASCADE)
# 	factory_name = models.CharField(max_length=32, unique=False, default=None, null=False, blank=False, verbose_name=u'工厂名')
# 	goods_name = models.CharField(max_length=20, unique=False, default=None, null=False, blank=False, verbose_name=u'货号')
# 	color = models.CharField(max_length=20, unique=False, default=None, null=False, blank=False, verbose_name=u'颜色')
# 	size = models.CharField(max_length=10, unique=False, default=None, null=False, blank=False, verbose_name=u'尺码')
# 	quantity = models.PositiveIntegerField(verbose_name=u'数量')
#
# 	class Meta:
# 		db_table = 'orderDetailsInfo'
# 		verbose_name = '订单详细'
# 		verbose_name_plural = verbose_name
#
# 	def __str__(self):
# 		return orderInfo.order_id

# class deliveryList(models.Model):
# 	delivery_id = models.CharField(max_length=32, unique=True, default=None, null=False, blank=False)
# 	delivery_date = models.DateField()
# 	delivery_traceID = models.CharField(max_length=20, unique=True, default=None, null=False, blank=False)
#
# 	class Meta:
# 		db_table = 'delivery_id'
# 		verbose_name = '发货列表'
# 		verbose_name_plural = verbose_name
#
# 	def __str__(self):
# 		return self.delivery_id
#
# class deliveryInfo(models.Model):
# 	delivery_id = models.ForeignKey("deliveryList")
# 	factory_name = models.CharField(max_length=32, unique=False, default=None, null=False, blank=False)
# 	goods_name = models.CharField(max_length=20, unique=False, default=None, null=False, blank=False)
# 	color = models.CharField(max_length=20, unique=False, default=None, null=False, blank=False)
# 	size = models.CharField(max_length=10, unique=False, default=None, null=False, blank=False)
# 	quantity = models.PositiveIntegerField()
#
# 	class Meta:
# 		db_table = 'deliveryDetailsInfo'
# 		verbose_name = '发货详细'
# 		verbose_name_plural = verbose_name
#
# 	def __str__(self):
# 		return deliveryInfo.delivery_id



