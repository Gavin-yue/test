from django.db import models
from manager.models import Type,Manager
# Create your models here.

class Goods(models.Model):
    class Meta():
        verbose_name="商品"
        verbose_name_plural="商品"
    goods_name=models.CharField(max_length=50,verbose_name='商品名称')
    goods_opice = models.FloatField(verbose_name='现价')
    goods_xprice=models.FloatField(verbose_name='原价')
    goods_count=models.IntegerField(default=0,verbose_name='商品数量')
    goods_production=models.DateField(auto_now=True,verbose_name='生产日期')
    safe_date = models.CharField(max_length=10,verbose_name='保质期')
    goods_method=models.CharField(max_length=100,verbose_name="存储方法")
    goods_description = models.CharField(max_length=100,verbose_name='商品简介')
    goods_pic=models.ImageField(upload_to='media/goods/image',verbose_name='商品图片')
    goods_addresss = models.CharField(max_length=50,verbose_name='配送地址')
    goods_info = models.TextField(verbose_name='商品详情')
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE,verbose_name='商家名称')
    type=models.ForeignKey(Type,on_delete=models.CASCADE,verbose_name='类别')
    status=models.BooleanField(default=1,verbose_name='商品状态')
    def __str__(self):
        return self.goods_name
