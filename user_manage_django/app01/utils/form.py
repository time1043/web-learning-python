from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from app01.models import UserInfo, PrettyNum, Admin
from app01.utils.bootstrap import BootStrapModelForm, BootStrapForm
from app01.utils.encrypt import md5_str


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
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)  # 保留原来的输入
    )

    class Meta:
        model = Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {'password': forms.PasswordInput(render_value=True)}

    def clean_password(self):
        """密码md5加密后存储到数据库"""
        pwd = self.cleaned_data.get('password')
        return md5_str(pwd)

    def clean_confirm_password(self):
        """验证两次密码一致"""
        pwd = self.cleaned_data.get('password')  # c21b074eef9e2e7fe68bd20cfc8a1224
        confirm = md5_str(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('两次密码不一致')
        return confirm  # 该字段写入数据库


class AdminEditModelForm(BootStrapModelForm):
    """编辑只允许用户名的修改"""

    class Meta:
        model = Admin
        fields = ['username']


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)  # 保留原来的输入
    )

    class Meta:
        model = Admin
        fields = ['password', 'confirm_password']
        widgets = {'password': forms.PasswordInput(render_value=True)}

    def clean_password(self):
        """密码md5加密后存储到数据库"""
        pwd = self.cleaned_data.get('password')
        pwd_md5 = md5_str(pwd)

        # 不允许和以前的密码一致 去数据库校验
        exists = Admin.objects.filter(id=self.instance.pk, password=pwd_md5).exists()
        if exists:
            raise ValidationError('重置密码不能和原密码一致')

        return pwd_md5

    def clean_confirm_password(self):
        """验证两次密码一致"""
        pwd = self.cleaned_data.get('password')  # c21b074eef9e2e7fe68bd20cfc8a1224
        confirm = md5_str(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('两次密码不一致')
        return confirm  # 该字段写入数据库


class LoginForm(BootStrapForm):
    """登录功能的表单，不用增删改查，只需要单纯的数据库校验"""
    username = forms.CharField(label='用户名', widget=forms.TextInput, required=True)
    password = forms.CharField(label='密码', widget=forms.PasswordInput(render_value=True), required=True)

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5_str(pwd)
