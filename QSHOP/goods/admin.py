from django.contrib import admin

# Register your models here.
from .models import Goods

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display=['id','goods_name','goods_opice']
    # date_hierachy='date'    #根据日期数据进行分类,实现搜索功能
