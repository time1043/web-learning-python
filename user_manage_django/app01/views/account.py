from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render, redirect

from app01.models import Admin
from app01.utils.check_code import create_check_code
from app01.utils.form import LoginForm


def login(request):
    """ 登录功能 """
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    # POST
    form = LoginForm(data=request.POST)
    if form.is_valid():

        # 验证码校验
        user_input_code = form.cleaned_data.pop('code')  # **form.cleaned_data
        image_code = request.session.get('image_code')  # 可能为空 60s
        if not image_code:
            form.add_error('code', '验证码超时')
            return render(request, 'login.html', {'form': form})
        if user_input_code.upper() != image_code.upper():  # 忽略大小写
            form.add_error('code', '验证码错误')
            return render(request, 'login.html', {'form': form})

        # 数据库校验
        admin_obj = Admin.objects.filter(**form.cleaned_data).first()  # dic
        if not admin_obj:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'login.html', {'form': form})

        # 校验正确：网站生成字符串，写到用户浏览器的cookie中，并且写道服务端的session中 (django封装)
        request.session['info'] = {'id': admin_obj.id, 'name': admin_obj.username}
        request.session.set_expiry(60 * 60 * 34 * 7)  # 7天有效
        return redirect('/admin/list/')  # 登录成功后重定向  select * from django_session;

    return render(request, 'login.html', {'form': form})


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect('/login/')


def image_code(request):
    """ 动态生成图片验证码 """
    img, code_str = create_check_code()
    request.session['image_code'] = code_str  # 后续需要校验 先写入session
    request.session.set_expiry(60)  # 设置60s超时

    # 不写入磁盘 而是在内存
    stream = BytesIO()
    img.save(stream, 'png')
    stream.getvalue()

    return HttpResponse(stream.getvalue())
