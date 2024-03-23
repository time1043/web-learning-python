from django.shortcuts import render, redirect

from app01.models import Department


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
#
#
# def depart_dlt(request):
#     """ 部门删除 """
#     depart_id = request.GET.get('nid')
#     Department.objects.filter(id=depart_id).delete()
#     return redirect('/depart/list/')
