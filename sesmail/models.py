#coding:utf-8
from django.db import models

# Create your models here.



class EmailAddress(models.Model):
    email = models.EmailField(u'邮件地址',max_length=255)   #邮件地址
    source = models.CharField(u'来源',max_length=255) #渠道来源
    email_type = models.CharField(max_length=255) # 分类  
    country  = models.CharField(max_length=255) #用于区别是内国还是国外
    author = models.CharField(max_length=255) #提供者
    department = models.CharField(max_length=255) #提供者的部门

    def __str__(self):    
        return self.email
    
    
    



    
    
    
    
    
        
