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


class PrettyNum(models.Model):
    """ 靓号表 """
    mobile = models.CharField(verbose_name='手机号码', max_length=11)  # 允许为空  null=True blank=True
    price = models.DecimalField(verbose_name='价格', default=0, max_digits=7, decimal_places=2)
    level_choices = ((1, '初级'), (2, '中级'), (3, '高级'))
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    status_choices = ((0, '未占用'), (1, '已占用'))
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=0)
