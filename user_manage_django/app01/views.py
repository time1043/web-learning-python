import requests
from django.shortcuts import render, HttpResponse, redirect

from app01.models import Department, UserInfo


def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return render(request, 'user_add.html')


def tpl(request):
    name = '周坚深'  # 模拟数据库拿取
    roles = ['员工', '组长', '经理', '工程师']
    user_info = {'name': '沈以容', 'salary': '50k', 'role': '工程师'}
    list_dict = [
        {'name': '沈以容', 'salary': '50k', 'role': '工程师'},
        {'name': '涂尔干', 'salary': '30k', 'role': '思想家'},
        {'name': '孟德斯鸠', 'salary': '40k', 'role': '思想家'}
    ]  # 列表里套字典
    return render(request, 'tpl.html', {'n1': name, 'n2': roles, 'n3': user_info, 'n4': list_dict})


def news(request):
    # 自己构造 or 数据库 or 网络请求
    url = 'http://www.chinaunicom.com/api/article/NewsByIndex/2/2023/08/news?fcjecbaaimohlnoh'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    resp = requests.get(url=url, headers=headers, allow_redirects=True)
    list_data = resp.json()
    print(list_data)
    return render(request, 'news.html', {'list_data': list_data})


def reqresp(request):  # request对象 封装了用户通过浏览器发送过来的所有请求数据
    print(request.method)  # 用户的请求方式 get
    print(request.GET)  # 接受用户在url上传递一些值 <QueryDict: {'n': ['123'], 'p': ['asd']}>

    # return HttpResponse('返回内容')  # 【响应】将指定内容响应
    # return render(request, 'reqresp.html', {'np': request.GET})  # 【响应】将指定内容响应  读取html + 渲染替换 -> 字符串
    return redirect('https://www.baidu.com')  # 【响应】重定向到其他网页


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    # 不是get而是post
    username = request.POST.get('user')
    password = request.POST.get('pwd')
    if username == 'root' and password == '123':
        return redirect('https://www.baidu.com')
    # 否则登录失败
    return render(request, 'login.html', {'error_msg': '用户名或密码错误'})


def orm(request):
    # 1 新增数据
    Department.objects.create(title='销售部')
    Department.objects.create(title='财务部')
    Department.objects.create(title='市场部')
    UserInfo.objects.create(name='周坚深', password='fgh', age='33')
    UserInfo.objects.create(name='沈以容', password='asd', age='22')
    # UserInfo.objects.create(name='林云', password='123')  # err

    # 2 删除数据
    UserInfo.objects.filter(name='林云').delete()
    Department.objects.all().delete()

    # 3 获取符合条件的数据
    list_date = UserInfo.objects.all()
    for obj in list_date:
        print(obj.id, obj.name, obj.password, obj.age)

    list_date = UserInfo.objects.filter(id=1)  # <QuerySet [<UserInfo: UserInfo object (1)>]>
    print(list_date)

    row_obj = UserInfo.objects.filter(id=1).first()  # 获取第一条数据  对象
    print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)

    # 4 更新数据
    UserInfo.objects.all().update(password=999)
    UserInfo.objects.filter(id=2).update(age=99)
    UserInfo.objects.filter(name='周坚深').update(age=43)

    return HttpResponse('成功')
    # return render(request, 'orm.html')
