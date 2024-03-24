from django.shortcuts import render, redirect

from app01.models import Department
from app01.utils.pagination import Pagination


def depart_list(request):
    """ 部门列表 """
    queryset = Department.objects.all()
    page_object = Pagination(request, queryset)
    context = {
        'list_depart': page_object.page_queryset,
        'page_string': page_object.html()
    }
    return render(request, 'depart/depart_list.html', context)


def depart_add(request):
    """ 部门添加 """
    if request.method == 'GET':
        return render(request, 'depart/depart_add.html')
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
        return render(request, 'depart/depart_edit.html', {'row': row})  # 传默认值
    # POST  获取用户提交数据  更新到数据库
    title = request.POST.get('title')
    Department.objects.filter(id=nid).update(title=title)
    return redirect('/depart/list/')  # 重定向
