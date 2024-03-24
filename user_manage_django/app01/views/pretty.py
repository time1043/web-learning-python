from django.shortcuts import render, redirect

from app01.models import PrettyNum
from app01.utils.form import PrettyEditModelForm, PrettyModelForm
from app01.utils.pagination import Pagination


def pretty_list(request):
    """ 靓号列表 """
    # 条件筛选
    data_dict = {}
    search_data = request.GET.get('q', '')  # 有值拿值 没值空字符串
    if search_data:  # 考虑空字典情况
        data_dict['mobile__contains'] = search_data

    # 自定义页码对象 实例化
    queryset = PrettyNum.objects.filter(**data_dict).order_by('-level')  # 搜索完的数据
    page_object = Pagination(request, queryset, page_size=18)  # page_size=20
    context = {
        'search_data': search_data,  # 条件筛选
        'list_pretty': page_object.page_queryset,  # 分完页的数据
        'page_string': page_object.html()  # 页码
    }

    return render(request, 'pretty/pretty_list.html', context)


def pretty_model_form_add(request):
    """ 新建靓号 """
    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, 'common/change_page.html', {'form': form, 'title': '添加靓号'})
    # POST
    form = PrettyModelForm(data=request.POST)  # 传默认数据
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    # 校验失败
    return render(request, 'common/change_page.html', {'form': form, 'title': '添加靓号'})  # 显示错误信息


def pretty_dlt(request):
    """ 删除靓号 """
    pretty_id = request.GET.get('nid')
    PrettyNum.objects.filter(id=pretty_id).delete()
    return redirect('/pretty/list/')


def pretty_model_form_edit(request, nid):
    """ 编辑靓号 """
    title = '编辑靓号'
    row = PrettyNum.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PrettyEditModelForm(instance=row)  # 默认值设置
        return render(request, 'common/change_page.html', {'form': form, 'title': title})
    # POST
    form = PrettyEditModelForm(data=request.POST, instance=row)  # 默认值填充
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    # 不合法数据
    return render(request, 'common/change_page.html', {'form': form, 'title': title})
