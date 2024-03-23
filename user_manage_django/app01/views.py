from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.shortcuts import render, redirect

from app01.models import Department, UserInfo


def depart_list(request):
    """ 部门列表 """
    list_depart = Department.objects.all()  # 数据库获取数据
    return render(request, 'depart_list.html', {'list_depart': list_depart})


def depart_add(request):
    """ 部门添加 """
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    # POST  获取用户提交数据  保存到数据库
    title = request.POST.get('title')
    Department.objects.create(title=title)
    return redirect('/depart/list/')  # 重定向


def depart_dlt(request):
    """ 部门删除 """
    depart_id = request.GET.get('nid')
    Department.objects.filter(id=depart_id).delete()
    return redirect('/depart/list/')


def depart_edit(request, nid):  # 编辑区别于添加  携带id
    """ 部门编辑 """
    if request.method == 'GET':
        row = Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row': row})  # 传默认值
    # POST  获取用户提交数据  更新到数据库
    title = request.POST.get('title')
    Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list/')  # 重定向


# ----------------------------------------------
def user_list(request):
    """ 用户列表 """
    list_user = UserInfo.objects.all()
    paginator = Paginator(list_user, 30)  # 每页显示10条数据

    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)  # 如果页数不是整数，显示第一页
    except EmptyPage:
        users = paginator.page(paginator.num_pages)  # 如果页数超出范围，显示最后一页

    return render(request, 'user_list.html', {'users': users})


def user_add(request):
    """ 用户添加 """
    if request.method == 'GET':
        return render(request, 'user_add.html', {
            'departments': Department.objects.all(),
            'gender_choices': UserInfo.gender_choices
        })
    # POST
    name = request.POST.get('username')
    password = request.POST.get('password')
    age = request.POST.get('age')
    account = request.POST.get('account')
    create_time = request.POST.get('create_time')  # 对违法数据疲软
    depart_id = request.POST.get('depart')
    gender = request.POST.get('gender')
    UserInfo.objects.create(name=name, password=password, age=age, account=account, create_time=create_time,
                            depart_id=depart_id, gender=gender)
    return redirect('/user/list/')


def user_dlt(request):
    """ 用户删除 """
    user_id = request.GET.get('nid')
    UserInfo.objects.filter(id=user_id).delete()
    return redirect('/user/list/')


def user_edit(request, nid):  # 编辑区别于添加  携带id
    """ 用户编辑 """
    if request.method == 'GET':
        row = UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'row': row, 'departments': Department.objects.all(),
                                                  'gender_choices': UserInfo.gender_choices})
    # POST
    name = request.POST.get('username')
    password = request.POST.get('password')
    age = request.POST.get('age')
    account = request.POST.get('account')
    create_time = request.POST.get('create_time')
    depart_id = request.POST.get('depart')
    gender = request.POST.get('gender')
    UserInfo.objects.filter(id=nid).update(name=name, password=password, age=age, account=account,
                                           create_time=create_time, depart_id=depart_id, gender=gender)
    return redirect('/user/list/')


# ----------------------------------------------
class UserModelForm(ModelForm):
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
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # if name == 'password':
            #     continue
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def user_model_form_add(request):
    """ 用户添加 model form """
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {'form': form})

    # POST  数据校验 用户提示
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 合法数据：{'name': 'time1043', 'password': '11', 'age': 1, 'account': Decimal('0'), 'create_time': datetime.datetime(2022, 11, 22, 12, 12, 12, tzinfo=backports.zoneinfo.ZoneInfo(key='UTC')), 'depart': <Department: HR (人力资源)>, 'gender': 1}
        form.save()  # django 保存到数据库中
        return redirect('/user/list/')

    # 校验失败 提示用户
    return render(request, 'user_model_form_add.html', {'form': form})


def user_model_form_edit(request, nid):
    """ 用户编辑 model form """
    row = UserInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = UserModelForm(instance=row)  # mf 设置默认值
        return render(request, 'user_model_form_edit.html', {'form': form})
    # POST
    form = UserModelForm(data=request.POST, instance=row)  # 变新增为提交
    if form.is_valid():
        # 默认保存的是用户输入的所有数据  若想保存用户没权限输入的数据
        # form.instance.字段名 = 值
        form.save()
        return redirect('/user/list/')
    # 不合法数据
    return render(request, 'user_model_form_edit.html', {'form': form})
