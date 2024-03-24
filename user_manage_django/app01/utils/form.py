from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from app01.models import UserInfo, PrettyNum, Admin
from app01.utils.bootstrap import BootStrapModelForm


class UserModelForm(BootStrapModelForm):
    # 额外加验证
    password_validator = RegexValidator(
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$',
        message="密码必须至少有8个字符，包括大小写字母和数字。"
    )
    name = forms.CharField(min_length=2, label='用户名')
    password = forms.CharField(label='密码', validators=[password_validator])  # 正则校验

    class Meta:
        model = UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'depart', 'gender']


class PrettyModelForm(BootStrapModelForm):
    class Meta:
        model = PrettyNum
        fields = '__all__'  # 所有字段

    def clean_mobile(self):  # 钩子方法
        txt_mobile = self.cleaned_data['mobile']

        # 不允许手机号码重复
        exists = PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('该手机号码已经存在')

        if len(txt_mobile) != 11:
            raise ValidationError('手机号码的格式有误')
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):
    class Meta:
        model = PrettyNum
        fields = ['mobile', 'price', 'level', 'status']  # 自定义选择字段

    def clean_mobile(self):  # 钩子方法
        txt_mobile = self.cleaned_data['mobile']

        # 手机号码不允许重复
        exists = PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile)  # 当前编辑的那一行id
        if exists:
            raise ValidationError('该手机号码已经存在')

        if len(txt_mobile) != 11:
            raise ValidationError('手机号码的格式有误')
        return txt_mobile


class AdminModelForm(BootStrapModelForm):
    class Meta:
        model = Admin
        fields = ['username', "password"]
