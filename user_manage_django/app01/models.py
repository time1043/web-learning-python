from datetime import datetime

from django.db import models


class Department(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name='标题', max_length=100)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='入职时间', default=datetime.now)

    depart = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)

    gender_choices = ((1, '男'), (0, '女'))  # 性别不会增减  字节占用少  django约束
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
