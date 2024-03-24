from django.shortcuts import render, redirect

from app01.models import Admin
from app01.utils.form import LoginForm


def login(request):
    """ 登录功能 """
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    # POST
    form = LoginForm(data=request.POST)
    if form.is_valid():

        # 数据库校验
        admin_obj = Admin.objects.filter(**form.cleaned_data).first()  # dic
        if not admin_obj:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'login.html', {'form': form})

        # 校验正确：网站生成字符串，写到用户浏览器的cookie中，并且写道服务端的session中 (django封装)
        request.session['info'] = {'id': admin_obj.id, 'name': admin_obj.username}
        return redirect('/admin/list/')  # 登录成功后重定向  select * from django_session;

    return render(request, 'login.html', {'form': form})
