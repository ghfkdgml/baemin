from django.db import models
from django.contrib.auth.models import User
from partner.models import Menu

class Client(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(verbose_name="고객명",max_length=50)
    contact=models.CharField(verbose_name="전화번호",max_length=50)
    address=models.CharField(verbose_name="주소",max_length=200)
    description=models.TextField(verbose_name="상세 소개",)
    def __str__(self):
        return self.name

class Order(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    address=models.CharField(
        max_length=100,
        verbose_name="주소",
    )
    created_at=models.DateTimeField(auto_now_add=True)
    items=models.ManyToManyField(Menu,through='OrderItem',through_fields=('order','menu'),)
    def __str__(self):
        return self.client.name

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE)
    count=models.PositiveIntegerField()
    def __str__(self):
        return self.menu.partner.name+' '+self.menu.name+' '+str(self.count)
