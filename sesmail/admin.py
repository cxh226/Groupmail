#coding=utf-8
from django.contrib import admin
from .models import EmailAddress

# Register your models here.

class   emaillist(admin.ModelAdmin):
    list_display =('email','source','email_type','country','author','department',)  #指定要显示的字段
    search_fields = ('email','source',)  #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter  = ('email',)   #指定列表过滤器，右边将会出现一个快捷的日期过滤选项， 同样你也可以指定非日期型类型的字段     
#     fields = ('email','author',)   #自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性



admin.site.register(EmailAddress,emaillist)
