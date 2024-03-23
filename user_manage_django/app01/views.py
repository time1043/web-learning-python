from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
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
