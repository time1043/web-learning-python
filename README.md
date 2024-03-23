# user-manage
这是用户中心项目，可以成为未来许多项目的基础。



- 定位

  flask：小巧、功能有限

  django：集成很多组件

- 参考

  [django官方文档](https://docs.djangoproject.com/zh-hans/4.2/)、[博客文章](https://www.cnblogs.com/wupeiqi/)、[交流博客](https://www.xinyan666.fun/article/article_list/)

  [Django 学习小组](https://zhuanlan.zhihu.com/djstudyteam)、[使用Django做个日程管理系统](https://zhuanlan.zhihu.com/p/52991783)





## 基础知识

### 环境创建

- 安装django

  ```
  conda info -e
  conda create -n forWeb python=3.8
  conda activate forWeb
  
  pip install django
  
  ```
  
  python文件结构
  

  > 1 python.exe
  >
  > 2 Scripts：pip.exe、创建项目的工具 `django-admin.exe`  // 加入环境变量
  >
  > 3 Lib：内置模块、site-packages(`第三方模块django框架源码`)

  创建项目 (命令行 pycharm)

  ```
  cd D:\code2\python-code\user-manage
  django-admin startproject user-manage-django
  
  # 命令行创建：最标准
  # pycharm创建：在标准的基础上多加templates、settings.py数据
  
  ```
  
  项目结构
  
  > 1 manage.py		// 项目管理：启动项目、创建app、数据管理		【直接用】
  >
  > 2 django230926项目同名文件夹
  >
  > ​	\_\_init__.py
  >
  > ​	asgi.py		// 接受网络请求																【不管】
  >
  > ​	wsgi.py		// 接受网络请求																【不管】
  >
  > ​	urls.py		// url和python函数对应关系																  【操作】
  >
  > ​	setting.py	 // 项目配置文件：数据库连接、注册app											【操作】
  
  
  
  



- 创建app (划分功能)

  app用户管理		// 独立的表结构 函数  HTMLCSS模板

  app订单管理		// 独立的表结构 函数  HTMLCSS模板

  app后台管理		// 独立的表结构 函数  HTMLCSS模板

  ```
  python manage.py startapp app01
  python manage.py startapp app02
  tree /f
  
  ```

  APP的文件结构

  ```
  (forWeb) user_manage_django>tree /f
  卷 软件 的文件夹 PATH 列表
  卷序列号为 6C7E-ECA6
  D:.
  │  manage.py
  │  
  ├─.idea
  │  │  .gitignore
  │  │  user_manage_django.iml
  │  │  misc.xml
  │  │  modules.xml
  │  │  workspace.xml
  │  │
  │  └─inspectionProfiles
  │          profiles_settings.xml
  │
  ├─app01
  │  │  admin.py		【不管】ajango后台管理
  │  │  apps.py		【不管】app启动类
  │  │  models.py		数据库操作【重要】
  │  │  tests.py		【不管】单元测试
  │  │  views.py		url对应的视图函数【重要】
  │  │  __init__.py
  │  │
  │  └─migrations		【不管】数据库变更记录
  │          __init__.py
  │
  ```

  

- 注册app

  user-manage\user_manage_django\user_manage_django\settings.py

  ```python
  
  INSTALLED_APPS = [
      'app01.apps.App01Config',
  ]
  
  ```

  [url](https://docs.djangoproject.com/en/3.2/topics/http/urls/)和视图函数的对应关系

  user-manage\user_manage_django\user_manage_django\urls.py

  ```python
  from django.contrib import admin
  from django.urls import path
  
  from app01 import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('index/', views.index)
  ]
  
  ```

  veiw函数 (接受用户请求)

  user-manage\user_manage_django\app01\views.py

  ```python
  from django.shortcuts import render, HttpResponse
  
  
  def index(request):
      return HttpResponse('欢迎使用')
  
  ```

  启动django项目 (命令行 pycharm)

  ```
  python manage.py runserver
  
  ```

  

### templates static

- 多个页面的url与view对应关系、templates模板 (想返回给用户html)

  ```
  mkdir -p app01/templates 
  mkdir -p app01/static/css app01/static/img app01/static/js app01/static/plugins
  
  ```

  ```python
  from django.shortcuts import render, HttpResponse
  
  
  def index(request):
      return render(request, "index.html")
  
  ```

  静态文件 (css js img)

  方法一：`<img src="../static/img/user_head.jpg">"`

  方法二：`{% load static %}`

  user_manage_django\app01\templates\index.html

  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>index</title>
          <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
      </head>
  
  
      <body>
          <script src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
          <script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.js' %}"></script>
          
          <h1>欢迎来到用户中心</h1>
          <img src="../static/img/user_head.jpg" alt="">
      </body>
  </html>
  ```

  user-manage\user_manage_django\user_manage_django\settings.py

  ```python
  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/3.2/howto/static-files/
  
  STATIC_URL = '/static/'
  
  ```

  

### 模板语法

- 作用：在HTML中写一些占位符，由数据对这些占位符进行替换和处理

  ![Snipaste_2023-11-02_21-01-36](res/Snipaste_2023-11-02_21-01-36.png)

  user_manage_django\user_manage_django\urls.py

  ```python
  from django.contrib import admin
  from django.urls import path
  
  from app01 import views
  
  urlpatterns = [
      path("admin/", admin.site.urls),
      path("index/", views.index),
      path('user/list/', views.user_list),
      path('user/add/', views.user_add),
      path('tpl/', views.tpl),
      path('news/', views.news),
      path('reqresp/', views.reqresp),
      path('login/', views.login),
      path('orm/', views.orm),
  ]
  ```

  user_manage_django\app01\views.py

  ```python
  from django.shortcuts import render, HttpResponse
  
  
  # Create your views here.
  
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
  
  ```

  user_manage_django\app01\templates\tpl.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>模板语法</title>
      </head>
      <body>
          <h1>模板语法</h1>
          <h3>单个变量</h3>
          <div>{{ n1 }}</div>
  
          <hr/>
          <h3>数组取值</h3>
          <div>{{ n2.0 }}</div>
          <div>{{ n2.1 }}</div>
          <div>{{ n2.2 }}</div>
  
          <h3>数组循环</h3>
          <div>
              {% for item in n2 %}
                  <span>{{ item }}</span>
              {% endfor %}
          </div>
  
          <hr/>
          <h3>字典取值</h3>
          <div>
              {{ n3 }}
              {{ n3.name }}
              {{ n3.salary }}
              {{ n3.role }}
          </div>
  
          <h3>循环字典的键</h3>
          <ul>
              {% for k in n3.keys %}
                  <li>{{ k }}</li>
              {% endfor %}
          </ul>
          <h3>循环字典的值</h3>
          <ul>
              {% for v in n3.values %}
                  <li>{{ v }}</li>
              {% endfor %}
          </ul>
          <h3>循环字典的键值对</h3>
          <ul>
              {% for k,v in n3.items %}
                  <li>{{ k }} ==> {{ v }}</li>
              {% endfor %}
          </ul>
  
          <hr/>
          <h3>列表里套字典</h3>
          {{ n4.1 }}
          {{ n4.1.role }}
  
          <h3>循环</h3>
          <table border="1">
              <thead>
                  <tr>
                      <th>Name</th>
                      <th>Salary</th>
                      <th>Role</th>
                  </tr>
              </thead>
              <tbody>
                  {% for item in n4 %}
                      <tr>
                          <td>{{ item.name }}</td>
                          <td>{{ item.salary }}</td>
                          <td>{{ item.role }}</td>
                      </tr>
                  {% endfor %}
              </tbody>
          </table>
  
          <hr/>
          <h3>条件语句</h3>
          {% if n1 == '沈以容' %}
              <h5>欢迎您，沈以容</h5>
          {% elif n1 == '周坚深' %}
              <h5>也欢迎您，周坚深</h5>
          {% else %}
              <h5>对不起，您是陌生用户</h5>
          {% endif %}
  
      </body>
  </html>
  
  ```

  

- 【案例】联通新闻中心

  ...

  



### 传递数据 (请求和响应)

- view函数处理

  ```python
  def reqresp(request):  # request对象 封装了用户通过浏览器发送过来的所有请求数据
      print(request.method)  # 用户的请求方式 get
      print(request.GET)  # 接受用户在url上传递一些值 <QueryDict: {'n': ['123'], 'p': ['asd']}>
  
      # return HttpResponse('返回内容')  # 【响应】将指定内容响应
      # return render(request, 'reqresp.html', {'np': request.GET})  # 【响应】将指定内容响应  读取html + 渲染替换 -> 字符串
      return redirect('https://www.baidu.com')  # 【响应】重定向到其他网页
  
  ```

  

- 【案例】用户登录

  django比flask多一层安全机制验证：`{% csrf_token %}`，否则是非法请求

  ```python
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
  ```

  ```html
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>欢迎登录</title>
      </head>
      <body>
          <h1>欢迎来到丑兮兮的登录界面</h1>
          <form method="post" action="/login/">
              {% csrf_token %}
              <input type="text" name="user" placeholder="用户名">
              <input type="password" name="pwd" placeholder="密码">
              <input type="submit" value="提交">
              <span style="color: red">{{ error_msg }}</span>
          </form>
      </body>
  </html>
  ```

  

### 数据库ORM操作

- MySQL数据库 + pymysql

  ```python
  import pymysql
  
  # 1.连接MySQL
  conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="root123", charset='utf8', db='unicom')
  cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
  
  # 2.发送指令
  cursor.execute("insert into admin(username,password,mobile) values('wupeiqi','qwe123','15155555555')")
  conn.commit()
  
  # 3.关闭
  cursor.close()
  conn.close()
  ```

  Django开发操作数据库更简单，内部提供了ORM框架

  ORM可以帮助我们做两件事：

  1 创建、修改、删除数据库中的表（不用你写SQL语句） 【无法创建数据库】

  2 操作表中的数据（不用你写SQL语句）

  ![Snipaste_2023-11-03_08-52-56](res/Snipaste_2023-11-03_08-52-56.png)

  
  
  
  
- [安装第三方模块支持](https://pypi.org/project/mysqlclient/#files)

  ```
  pip install mysqlclient
  
  ```

  自己创建数据库

  ```
  mysql -uroot -p123456
  create database forWeb;
  use forWeb;
  
  ```

  django连接数据库

  D:\code2\python-code\user-manage\user_manage_django\user_manage_django\settings.py

  ```python
  # Database
  # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'forWeb',
          'USER': 'root',
          'PASSWORD': '123456',
          'HOST': '127.0.0.1',
          'PORT': '3306',
      }
  }
  ```
  
  
  
- django操作表结构

  创建表、删除表、修改表

  D:\code2\python-code\user-manage\user_manage_django\app01\models.py (创建表)

  ```python
  from django.db import models
  
  
  class UserInfo(models.Model):
      name = models.CharField(max_length=32)
      password = models.CharField(max_length=32)
      age = models.IntegerField()
      # ORM根据相关信息自己写sql
  
  
  """
  create table app01_userinfo(
      id bignit auto_increment primary key,
      name varchar(32),
      password varchar(32),
      age int
  );
  """
  ```
  
  执行使得ORM转化为sql (在当前项目的根目录)
  
  ```
  python manage.py makemigrations  # 为这些更改创建迁移  用来修改数据库结构(而不是数据)  时间戳
  python manage.py migrate  # 应用那些由makemigrations创建的迁移
  # desc app01_userinfo;
  
  ```
  
  增加表删除表
  
  ```python
  class Department(models.Model):
      title = models.CharField(max_length=16)
  
  
  # class Role(models.Model):
  #     caption = models.CharField(max_length=16)
  ```
  
  在表中新增列
  
  ```python
  class UserInfo(models.Model):
      name = models.CharField(max_length=32)
      password = models.CharField(max_length=32)
      age = models.IntegerField(default=2)
      # size = models.IntegerField()
      
  """
  在表中新增列时，由于已存在列中可能已有数据，所以新增列必须要指定新增列对应的数据：
  1 手动输入一个值
  2 设置默认值  age = models.IntegerField(default=2)
  3 允许为空  data = models.IntegerField(null=True, blank=True)
  
  
  以后在开发中如果想要对表结构进行调整：
  在models.py文件中操作类即可
  python manage.py makemigrations
  python manage.py migrate
  """
  ```
  
  

- 填表中的数据

  views.py

  ```python
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
  ```

  

  

## 用户管理

- 用户管理

  1 展示用户列表：urls、函数(获取用户数据、html渲染)

  2 添加用户：urls、函数(get看到页面、post提交)

  3 删除用户：urls、函数、加入info_list.html

  

  路由

  ```
  from django.contrib import admin
  from django.urls import path
  
  from app01 import views
  
  urlpatterns = [
      path("admin/", admin.site.urls),
      path("depart/list/", views.depart_list),
      path("depart/add/", views.depart_add),
      path("depart/dlt/", views.depart_dlt),
  ]
  ```

  视图函数

  ```python
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
  
  
  def depart_dlt(request):
      """ 部门删除 """
      depart_id = request.GET.get('nid')
      Department.objects.filter(id=depart_id).delete()
      return redirect('/depart/list/')
  ```

  

  1



























