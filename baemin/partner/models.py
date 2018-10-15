from django.db import models
from django.contrib.auth.models import User

class Partner(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(verbose_name="업체이름",max_length=50)
    contact=models.CharField(verbose_name="전화번호",max_length=50)
    address=models.CharField(verbose_name="주소",max_length=200)
    description=models.TextField(verbose_name="상세 소개",)

class Menu(models.Model):
    partner=models.ForeignKey(Partner,on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="메뉴 이미지")
    name=models.CharField(verbose_name="메뉴 이름",max_length=50)
    price=models.PositiveIntegerField(verbose_name="메뉴 가격")
    def __str__(self):
        return self.partner.name +' '+self.name
