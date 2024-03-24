from django.shortcuts import render, redirect

from app01.models import Admin
from app01.utils.form import AdminModelForm, AdminEditModelForm, AdminResetModelForm
from app01.utils.pagination import Pagination


def admin_list(request):
    """ 管理员列表 """
    # 构造搜索条件
    data_dict = {}
    search_data = request.GET.get('q', '')  # 有值拿值 没值空字符串
    if search_data:  # 考虑空字典情况
        data_dict['username__contains'] = search_data
    # 根据搜索条件去数据库获取
    queryset = Admin.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)
    context = {
        'search_data': search_data,  # 条件筛选
        'list_admin': page_object.page_queryset,  # 分完页的数据
        'page_string': page_object.html()  # 页码
    }
    return render(request, 'myadmin/admin_list.html', context)


def admin_add(request):
    """ 管理员添加 """
    title = '新建管理员'
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'common/change_page.html', {'form': form, 'title': title})
    # POST
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    # 检验失败
    return render(request, 'common/change_page.html', {'form': form, 'title': title})


def admin_dlt(request):
    """ 管理员删除 """
    admin_id = request.GET.get('nid')
    Admin.objects.filter(id=admin_id).delete()
    return redirect('/admin/list/')


def admin_edit(request, nid):
    """ 管理员编辑 """
    title = '编辑管理员'
    row = Admin.objects.filter(id=nid).first()  # 数据库查询：对象、None
    if not row:
        return render(request, 'error/404.html', {'msg': '404：请求资源不存在，请检查您的操作'})

    # 数据库存在该对象
    if request.method == 'GET':
        form = AdminEditModelForm(instance=row)
        return render(request, 'common/change_page.html', {'form': form, 'title': title})
    # POST
    form = AdminEditModelForm(data=request.POST, instance=row)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    # 不合法数据
    return render(request, 'common/change_page.html', {'form': form, 'title': title})


def reset_pwd(request, nid):
    """ 不允许查看密码，但允许重置密码 """
    row = Admin.objects.filter(id=nid).first()  # 数据库查询：对象、None
    if not row:
        return render(request, 'error/404.html', {'msg': '404：请求资源不存在，请检查您的操作'})

    # 数据库存在该对象
    title = '重置密码 - {}'.format(row.username)
    if request.method == 'GET':
        form = AdminResetModelForm()
        return render(request, 'common/change_page.html', {'form': form, 'title': title})
    # POST
    form = AdminResetModelForm(data=request.POST, instance=row)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    # 不合法数据
    return render(request, 'common/change_page.html', {'form': form, 'title': title})
