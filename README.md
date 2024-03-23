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
  cd D:\code2\python-code\user-manage-learning
  django-admin startproject user_manage_django
  
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

  

  

### 【案例】用户管理

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

  D:\code2\python-code\user-manage\user_manage_django\app01\templates\depart_list.html

  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>部门列表</title>
          <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
      </head>
  
  
      <body>
          <script src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
          <script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.js' %}"></script>
  
          <!--导航栏-->
          <nav class="navbar navbar-default">
              <div class="container">
                  <!-- Brand and toggle get grouped for better mobile display -->
                  <div class="navbar-header">
                      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                              data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                          <span class="sr-only">Toggle navigation</span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                      </button>
                      <a class="navbar-brand" href="#">员工用户管理系统</a>
                  </div>
  
                  <!-- Collect the nav links, forms, and other content for toggling -->
                  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                      <ul class="nav navbar-nav">
                          <li><a href="/depart/list">部门管理</a></li>
                          <li><a href="#">用户管理</a></li>
                      </ul>
                      <ul class="nav navbar-nav navbar-right">
                          <li><a href="#">登录</a></li>
                          <li class="dropdown">
                              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                 aria-haspopup="true" aria-expanded="false">周坚深 <span class="caret"></span></a>
                              <ul class="dropdown-menu">
                                  <li><a href="#">个人资料</a></li>
                                  <li><a href="#">我的信息</a></li>
                                  <li role="separator" class="divider"></li>
                                  <li><a href="#">注销</a></li>
                              </ul>
                          </li>
                      </ul>
                  </div><!-- /.navbar-collapse -->
              </div><!-- /.container-fluid -->
          </nav>
  
          <!--主界面-->
          <div>
              <div class="container">
                  <!--按钮-->
                  <div style="margin-bottom: 10px">
                      <a class="btn btn-success" href="/depart/add/">
                          <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
                          新建部门
                      </a>
                  </div>
  
                  <!--表格 面板-->
                  <div class="panel panel-default">
                      <!-- Default panel contents -->
                      <div class="panel-heading"><font style="vertical-align: inherit;"><font
                              style="vertical-align: inherit;">
                          <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
                          部门列表
                      </font></font></div>
  
                      <!-- Table -->
                      <table class="table">
                          <thead>
                              <tr>
                                  <th><font style="vertical-align: inherit;"><font
                                          style="vertical-align: inherit;">ID</font></font></th>
                                  <th><font style="vertical-align: inherit;"><font
                                          style="vertical-align: inherit;">名称</font></font></th>
                                  <th><font style="vertical-align: inherit;"><font
                                          style="vertical-align: inherit;">操作</font></font></th>
                              </tr>
                          </thead>
                          <tbody>
                              {% for depart in list_depart %}
                                  <tr>
                                      <th scope="row"><font style="vertical-align: inherit;"><font
                                              style="vertical-align: inherit;">{{ depart.id }}</font></font></th>
                                      <td><font style="vertical-align: inherit;"><font
                                              style="vertical-align: inherit;">{{ depart.title }}</font></font></td>
                                      <td><font style="vertical-align: inherit;"><font
                                              style="vertical-align: inherit;">
                                          <a class="btn btn-primary btn-xs">编辑</a>
                                          <a class="btn btn-danger btn-xs" href="/depart/dlt/?nid={{ depart.id }}">删除</a>
                                      </font></font></td>
                                  </tr>
                              {% endfor %}
                          </tbody>
                      </table>
                  </div>
  
              </div>
          </div>
      </body>
  </html>
  ```

  D:\code2\python-code\user-manage\user_manage_django\app01\templates\depart_list.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>添加用户界面</title>
      </head>
      <body>
          <h1>添加用户界面</h1>
          <form method="post">
              {% csrf_token %}
              <input type="text" name="user" placeholder="用户名">
              <input type="text" name="pwd" placeholder="密码">
              <input type="text" name="age" placeholder="年龄">
              <input type="submit" value="提交">
          </form>
      </body>
  </html>
  ```

  



## 员工管理系统

### 环境准备

#### 创建项目注册app

- 项目环境

  命令行

  ```
  cd /d/code2/python-code/user-manage-learning/
  rm -rf user_manage_django/
  
  cd D:\code2\python-code\user-manage-learning
  django-admin startproject user_manage_django
  
  ```

  pycharm创建项目

  1 删除templates文件夹

  2 配置settings: "DIRS": [],

  settings.py

  ```python
  
  TEMPLATES = [
      {
          "BACKEND": "django.template.backends.django.DjangoTemplates",
          "DIRS": [],
          "APP_DIRS": True,
          "OPTIONS": {
              "context_processors": [
                  "django.template.context_processors.debug",
                  "django.template.context_processors.request",
                  "django.contrib.auth.context_processors.auth",
                  "django.contrib.messages.context_processors.messages",
              ],
          },
      },
  ]
  
  ```

  

- 创建app

  ```
   python manage.py startapp app01
   
  ```

  注册app settings.py

  ```python
  
  INSTALLED_APPS = [
      "django.contrib.admin",
      "django.contrib.auth",
      "django.contrib.contenttypes",
      "django.contrib.sessions",
      "django.contrib.messages",
      "django.contrib.staticfiles",
      'app01.apps.App01Config',
  ]
  
  ```

  

#### 数据库环境

- 数据库环境

  设计表结构

  ![Snipaste_2023-11-03_20-17-47](res/Snipaste_2023-11-03_20-17-47.png)

  部门ID需不需要约束？只能是部门表中已存在ID  `depart = models.ForeignKey(to='与哪张表关联', to_field='与这张表的哪一列关联')  # 报错`  

  (django内部：depart -> depart_id)

  部门被删除，关联的用户？删除用户，级联删除  `depart = models.ForeignKey(to='', to_field='', on_delete=models.CASCADE)`

  部门被删除，关联的用户？部门ID列置空  `depart = models.ForeignKey(to='', to_field='', null=True, blank=True, on_delete=models.SET_NULL)`

  

  D:\code2\python-code\user-manage-learning\user_manage_django\app01\models.py (代码集合)

  ```python
  from django.db import models
  
  
  class Department(models.Model):
      ''' 部门表 '''
      title = models.CharField(verbose_name='标题', max_length=100)
  
      def __str__(self):
          return self.title
  
  
  class UserInfo(models.Model):
      ''' 员工表 '''
      name = models.CharField(verbose_name='姓名', max_length=16)
      password = models.CharField(verbose_name='密码', max_length=64)
      age = models.IntegerField(verbose_name='年龄')
      account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
      create_time = models.DateTimeField(verbose_name='入职时间')
  
      depart = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)
  
      gender_choices = ((1, '男'), (0, '女'))  # 性别不会增减  字节占用少  django约束
      gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
  ```

  

- 数据库连接

  ```
  drop database forWeb2;
  create database forWeb2;
  use forWeb2;
  
  ```

  settings.py

  ```python
  # Database
  # https://docs.djangoproject.com/en/4.1/ref/settings/#databases
  
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'forWeb2',
          'USER': 'root',
          'PASSWORD': '123456',
          'HOST': '127.0.0.1',
          'PORT': '3306',
      }
  }
  ```

  ```
  python manage.py makemigrations
  python manage.py migrate
  
  ```

  

#### 工具类 (假数据生成)

- 生成一些假数据

  ```
  mkdir utils && touch utils/generate_data.py
  
  ```

  D:\code2\python-code\user-manage-learning\user_manage_django\utils\generate_data.py

  ```python
  import datetime
  import os
  import random
  import string
  
  import django
  from django.utils import timezone
  from faker import Faker
  
  # 确保在导入任何Django模块之前设置环境变量和初始化Django
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_manage_django.settings")
  django.setup()
  
  from app01.models import Department, UserInfo
  
  
  def create_data_to_department():
      # 读取文件
      department_names = []
      with open('departments_name.txt', 'r', encoding='utf-8') as file:
          for line in file:
              department_names.append(line.strip())
      print(department_names)
      # 添加到数据库中
      for dept in department_names:
          Department.objects.create(title=dept)
  
  
  """
  def generate_random_password(length=8):
      characters = string.ascii_letters + string.digits
      return ''.join(random.choice(characters) for i in range(length))
  """
  
  
  def generate_random_password(length=8):
      if length < 3:
          raise ValueError("ensure the password contains an uppercase, a lowercase, and a number.")
      # 先确保至少有一个大写字母、一个小写字母和一个数字
      password = [
          random.choice(string.ascii_lowercase),
          random.choice(string.ascii_uppercase),
          random.choice(string.digits)
      ]
      # 填充剩下的长度
      for i in range(length - 3):
          characters = string.ascii_letters + string.digits
          password.append(random.choice(characters))
      # 打乱字符的顺序以确保随机性
      random.shuffle(password)
      return ''.join(password)
  
  
  def create_data_to_userinfo(count):
      for _ in range(count):
          naive_datetime = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)  # 无时区信息
          aware_datetime = timezone.make_aware(naive_datetime, timezone.get_default_timezone())  # 转换为有时区信息的对象
  
          user = UserInfo(
              name=fake.name(),
              password=generate_random_password(),
              age=fake.random_int(min=20, max=60),
              account=fake.pydecimal(left_digits=8, right_digits=2, positive=True),
              create_time=aware_datetime,
              depart=random.choice(Department.objects.all()),
              gender=fake.random_element(elements=[0, 1])
          )
          user.save()
  
  
  if __name__ == '__main__':
      fake = Faker('zh_CN')
      create_data_to_department()
      create_data_to_userinfo(1000)
  
  ```

  

#### 静态文件和模板文件

- 静态文件模板文件的准备

  ```
  mkdir -p app01/templates 
  mkdir -p app01/static/css app01/static/img app01/static/js app01/static/plugins
  ```

  



### 部门管理和用户管理

#### 原生解 

- 页面设计

  ![Snipaste_2023-11-03_21-26-19](res/Snipaste_2023-11-03_21-26-19.png)

  路由注册 urls.py  (代码集合)

  ```python
  from django.contrib import admin
  from django.urls import path
  
  from app01 import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      
      # 部门管理
      path("depart/list/", views.depart_list),
      path("depart/add/", views.depart_add),
      path("depart/dlt/", views.depart_dlt),
      path("depart/<int:nid>/edit/", views.depart_edit),
  
      # 用户管理
      path("user/list/", views.user_list),
      path("user/add/", views.user_add),
      path("user/dlt/", views.user_dlt),
      path("user/<int:nid>/edit/", views.user_edit),
  ]
  ```

  视图函数 views.py  (代码集合)

  ```python
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
  
  ```

  

- 接口处理

  部门列表：

  新建部门：depart_list链接depart_add.html、urls、views)

  删除功能：urls、views) (加入depart_list.html 本页面完成)

  编辑页面：urls、views) (携带id：django正则) (传默认值)

  depart_list.html

  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>部门列表</title>
          <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
      </head>
  
  
      <body>
          <script src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
          <script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.js' %}"></script>
  
          <!--导航栏-->
          <nav class="navbar navbar-default">
              <div class="container">
                  <!-- Brand and toggle get grouped for better mobile display -->
                  <div class="navbar-header">
                      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                              data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                          <span class="sr-only">Toggle navigation</span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                      </button>
                      <a class="navbar-brand" href="#">员工用户管理系统</a>
                  </div>
  
                  <!-- Collect the nav links, forms, and other content for toggling -->
                  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                      <ul class="nav navbar-nav">
                          <li><a href="/depart/list">部门管理</a></li>
                          <li><a href="#">用户管理</a></li>
                      </ul>
                      <ul class="nav navbar-nav navbar-right">
                          <li><a href="#">登录</a></li>
                          <li class="dropdown">
                              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                 aria-haspopup="true" aria-expanded="false">周坚深 <span class="caret"></span></a>
                              <ul class="dropdown-menu">
                                  <li><a href="#">个人资料</a></li>
                                  <li><a href="#">我的信息</a></li>
                                  <li role="separator" class="divider"></li>
                                  <li><a href="#">注销</a></li>
                              </ul>
                          </li>
                      </ul>
                  </div><!-- /.navbar-collapse -->
              </div><!-- /.container-fluid -->
          </nav>
  
          <!--主界面-->
          <div>
              <div class="container">
                  <!--按钮-->
                  <div style="margin-bottom: 10px">
                      <a class="btn btn-success" href="/depart/add/">
                          <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
                          新建部门
                      </a>
                  </div>
  
                  <!--表格 面板-->
                  <div class="panel panel-default">
                      <!-- Default panel contents -->
                      <div class="panel-heading"><font style="vertical-align: inherit;"><font
                              style="vertical-align: inherit;">
                          <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
                          部门列表
                      </font></font></div>
  
                      <!-- Table -->
                      <table class="table">
                          <thead>
                              <tr>
                                  <th><font style="vertical-align: inherit;"><font
                                          style="vertical-align: inherit;">ID</font></font></th>
                                  <th><font style="vertical-align: inherit;"><font
                                          style="vertical-align: inherit;">名称</font></font></th>
                                  <th><font style="vertical-align: inherit;"><font
                                          style="vertical-align: inherit;">操作</font></font></th>
                              </tr>
                          </thead>
                          <tbody>
                              {% for depart in list_depart %}
                                  <tr>
                                      <th scope="row"><font style="vertical-align: inherit;"><font
                                              style="vertical-align: inherit;">{{ depart.id }}</font></font></th>
                                      <td><font style="vertical-align: inherit;"><font
                                              style="vertical-align: inherit;">{{ depart.title }}</font></font></td>
                                      <td><font style="vertical-align: inherit;"><font
                                              style="vertical-align: inherit;">
                                          <a class="btn btn-primary btn-xs" href="/depart/{{ depart.id }}/edit/">编辑</a>
                                          <a class="btn btn-danger btn-xs"
                                             href="/depart/dlt/?nid={{ depart.id }}">删除</a>
                                      </font></font></td>
                                  </tr>
                              {% endfor %}
                          </tbody>
                      </table>
                  </div>
  
              </div>
          </div>
      </body>
  </html>
  ```

  depart_add.html
  
  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>部门添加</title>
          <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
      </head>
  
  
      <body>
          <script src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
          <script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.js' %}"></script>
  
          <!--导航栏-->
          <nav class="navbar navbar-default">
              <div class="container">
                  <!-- Brand and toggle get grouped for better mobile display -->
                  <div class="navbar-header">
                      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                              data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                          <span class="sr-only">Toggle navigation</span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                      </button>
                      <a class="navbar-brand" href="#">员工用户管理系统</a>
                  </div>
  
                  <!-- Collect the nav links, forms, and other content for toggling -->
                  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                      <ul class="nav navbar-nav">
                          <li><a href="/depart/list">部门管理</a></li>
                          <li><a href="#">用户管理</a></li>
                      </ul>
                      <ul class="nav navbar-nav navbar-right">
                          <li><a href="#">登录</a></li>
                          <li class="dropdown">
                              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                 aria-haspopup="true" aria-expanded="false">周坚深 <span class="caret"></span></a>
                              <ul class="dropdown-menu">
                                  <li><a href="#">个人资料</a></li>
                                  <li><a href="#">我的信息</a></li>
                                  <li role="separator" class="divider"></li>
                                  <li><a href="#">注销</a></li>
                              </ul>
                          </li>
                      </ul>
                  </div><!-- /.navbar-collapse -->
              </div><!-- /.container-fluid -->
          </nav>
  
          <!--表单 面板-->
          <div>
              <div class="container">
                  <div class="panel panel-default">
                      <div class="panel-heading">
                          <h3 class="panel-title">新建部门</h3>
                      </div>
                      <div class="panel-body">
  
                          <!--表单-->
                          <form method="post">
                              {% csrf_token %}
                              <div class="form-group">
                                  <label>标题</label>
                                  <input type="text" class="form-control" placeholder="标题" name="title">
                              </div>
                              <button type="submit" class="btn btn-primary">提 交</button>
                          </form>
  
                      </div>
                  </div>
              </div>
          </div>
  
      </body>
  </html>
  ```
  
  depart_edit.html
  
  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>部门编辑</title>
          <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
      </head>
  
  
      <body>
          <script src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
          <script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.js' %}"></script>
  
          <!--导航栏-->
          <nav class="navbar navbar-default">
              <div class="container">
                  <!-- Brand and toggle get grouped for better mobile display -->
                  <div class="navbar-header">
                      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                              data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                          <span class="sr-only">Toggle navigation</span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                      </button>
                      <a class="navbar-brand" href="#">员工用户管理系统</a>
                  </div>
  
                  <!-- Collect the nav links, forms, and other content for toggling -->
                  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                      <ul class="nav navbar-nav">
                          <li><a href="/depart/list">部门管理</a></li>
                          <li><a href="#">用户管理</a></li>
                      </ul>
                      <ul class="nav navbar-nav navbar-right">
                          <li><a href="#">登录</a></li>
                          <li class="dropdown">
                              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                 aria-haspopup="true" aria-expanded="false">周坚深 <span class="caret"></span></a>
                              <ul class="dropdown-menu">
                                  <li><a href="#">个人资料</a></li>
                                  <li><a href="#">我的信息</a></li>
                                  <li role="separator" class="divider"></li>
                                  <li><a href="#">注销</a></li>
                              </ul>
                          </li>
                      </ul>
                  </div><!-- /.navbar-collapse -->
              </div><!-- /.container-fluid -->
          </nav>
  
          <!--表单 面板-->
          <div>
              <div class="container">
                  <div class="panel panel-default">
                      <div class="panel-heading">
                          <h3 class="panel-title">编辑部门</h3>
                      </div>
                      <div class="panel-body">
  
                          <!--表单-->
                          <form method="post">
                              {% csrf_token %}
                              <div class="form-group">
                                  <label>标题</label>
                                  <input type="text" class="form-control" placeholder="标题" name="title"
                                         value="{{ row.title }}">
                              </div>
                              <button type="submit" class="btn btn-primary">提 交</button>
                          </form>
  
                      </div>
                  </div>
              </div>
          </div>
  
      </body>
  </html>
  ```
  
  

- url传递动态值

  ```
  urls.py
  path("depart/<int:nid>/edit/", views.depart_edit),
  
  depart_list.html
  <a class="btn btn-primary btn-xs" href="/depart/{{ depart.id }}/edit/">编辑</a>
  
  ```

  

- 用戶管理 (单例代码)

  user_list的views

  ```python
  def user_list(request):
      """ 用户列表 """
      list_user = UserInfo.objects.all()
      for user in list_user[:2]:
          print(user.create_time.strftime('%Y-%m-%d'))
          print(user.get_gender_display())  # django封装
          print(user.depart.title)  # django 跨表获取
      return render(request, 'user_list.html', {'list_user': list_user})
  ```

  user_list的html

  ```html
  <tr>
      <th scope="row"><font style="vertical-align: inherit;"><font
              style="vertical-align: inherit;">{{ user.id }}</font></font></th>
      <td><font style="vertical-align: inherit;"><font
              style="vertical-align: inherit;">{{ user.name }}</font></font></td>
      <td><font style="vertical-align: inherit;"><font
              style="vertical-align: inherit;">{{ user.password }}</font></font></td>
      <td><font style="vertical-align: inherit;"><font
              style="vertical-align: inherit;">{{ user.age }}</font></font></td>
      <td><font style="vertical-align: inherit;"><font
              style="vertical-align: inherit;">{{ user.account }}</font></font></td>
      <td><font style="vertical-align: inherit;"><font
              style="vertical-align: inherit;">{{ user.create_time|date:'Y-m-d h:i:s' }}</font></font></td>
      <td><font style="vertical-align: inherit;"><font
              style="vertical-align: inherit;">{{ user.get_gender_display }}</font></font></td>
      <td><font style="vertical-align: inherit;"><font
              style="vertical-align: inherit;">{{ user.depart.title }}</font></font></td>
      <td><font style="vertical-align: inherit;"><font
              style="vertical-align: inherit;">
          <a class="btn btn-primary btn-xs" href="/depart/{{ depart.id }}/edit/">编辑</a>
          <a class="btn btn-danger btn-xs"
             href="/depart/dlt/?nid={{ depart.id }}">删除</a>
      </font></font></td>
  </tr>
  ```

  user_add的views

  ```python
  def user_add(request):
      """ 用户添加 """
      if request.method == 'GET':
          return render(request, 'user_add.html', {
              'departments': Department.objects.all(),
              'gender_choices': UserInfo.gender_choices
          })
  ```

  user_add的html

  ```html
  <!--表单-->
  <form method="post">
      {% csrf_token %}
      <div class="form-group">
          <label>姓名</label>
          <input type="text" class="form-control" placeholder="姓名" name="username">
          <label>密码</label>
          <input type="password" class="form-control" placeholder="密码" name="password">
          <label>年龄</label>
          <input type="number" class="form-control" placeholder="年龄" name="age">
          <label>账户余额</label>
          <input type="number" step="0.01" class="form-control" placeholder="账户余额" name="account">
  
          <!--<label>入职时间</label>
          <input type="data" class="form-control" placeholder="入职时间" name="create_time">
          <label>所属部门</label>
          <input type="text" class="form-control" placeholder="所属部门" name="depart_id">
          <label>性别</label>
          <input type="text" class="form-control" placeholder="性别" name="gender">-->
  
          <label>入职时间</label>
          <input type="datetime-local" name="create_time" class="form-control">
  
          <label>所属部门</label>
          <select name="depart" class="form-control">
              {% for dept in departments %}
                  <option value="{{ dept.id }}">{{ dept.title }}</option>
              {% endfor %}
          </select>
  
          <label>性别</label>
          <div>
              {% for value, name in gender_choices %}
                  <label class="radio-inline">
                      <input type="radio" name="gender" value="{{ value }}"> {{ name }}
                  </label>
              {% endfor %}
          </div>
  
      </div>
      <button type="submit" class="btn btn-primary">提 交</button>
  </form>
  ```

  user_list的html的dlt按钮

  ```html
                                  <a class="btn btn-danger btn-xs"
                                     href="/user/dlt/?nid={{ user.id }}">删除</a>
  ```

  user_edit的views

  ```python
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
  ```

  user_edit的html

  ```html
  <!--表单-->
  <form method="post">
      {% csrf_token %}
      <div class="form-group">
          <label>姓名</label>
          <input type="text" class="form-control" placeholder="姓名" name="username"
                 value="{{ row.name }}">
          <label>密码</label>
          <input type="password" class="form-control" placeholder="密码" name="password"
                 value="{{ row.password }}">
          <label>年龄</label>
          <input type="number" class="form-control" placeholder="年龄" name="age" value="{{ row.age }}">
          <label>账户余额</label>
          <input type="number" step="0.01" class="form-control" placeholder="账户余额" name="account"
                 value="{{ row.account }}">
  
          <label>入职时间</label>
          <input type="datetime-local" name="create_time" class="form-control"
                 value="{{ row.create_time|date:'Y-m-d\TH:i' }}">
  
          <label>所属部门</label>
          <select name="depart" class="form-control">
              {% for dept in departments %}
                  <option value="{{ dept.id }}" {% if row.depart.id == dept.id %}selected{% endif %}>
                      {{ dept.title }}
                  </option>
              {% endfor %}
          </select>
  
          <label>性别</label>
          <div>
              {% for value, name in gender_choices %}
                  <label class="radio-inline">
                      <input type="radio" name="gender" value="{{ value }}"
                             {% if row.gender == value %}checked{% endif %}>
                      {{ name }}
                  </label>
              {% endfor %}
          </div>
  
      </div>
      <button type="submit" class="btn btn-primary">提 交</button>
  </form>
  ```

  



#### 模板继承

- 简化

  部门列表、添加部门、编辑部门  ——  拷贝导航栏、引入  ——  固定的、动态的

  

  定义母版layout.html

  ```
  {% load static %}
  
      {% block css %}{% endblock %}
      {% block js %}{% endblock %}
      {% block content %}{% endblock %}
  ```

  继承母版

  ```
  {% extends 'layout.html' %}
  
  {% block css %}{% endblock %}
  {% block content %}{% endblock %}
  {% block js %}{% endblock %}
  ```

  

- 部门管理

  layout.html

  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>员工管理系统</title>
          <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
          {% block css %}{% endblock %}
      </head>
  
  
      <body>
          <!--导航栏-->
          <nav class="navbar navbar-default">
              <div class="container">
                  <!-- Brand and toggle get grouped for better mobile display -->
                  <div class="navbar-header">
                      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                              data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                          <span class="sr-only">Toggle navigation</span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                      </button>
                      <a class="navbar-brand" href="#">员工用户管理系统</a>
                  </div>
  
                  <!-- Collect the nav links, forms, and other content for toggling -->
                  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                      <ul class="nav navbar-nav">
                          <li><a href="/depart/list/">部门管理</a></li>
                          <li><a href="/user/list/">用户管理</a></li>
                      </ul>
                      <ul class="nav navbar-nav navbar-right">
                          <li><a href="#">登录</a></li>
                          <li class="dropdown">
                              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                 aria-haspopup="true" aria-expanded="false">周坚深 <span class="caret"></span></a>
                              <ul class="dropdown-menu">
                                  <li><a href="#">个人资料</a></li>
                                  <li><a href="#">我的信息</a></li>
                                  <li role="separator" class="divider"></li>
                                  <li><a href="#">注销</a></li>
                              </ul>
                          </li>
                      </ul>
                  </div><!-- /.navbar-collapse -->
              </div><!-- /.container-fluid -->
          </nav>
  
          <!--主界面-->
          <div>
              {% block content %}{% endblock %}
          </div>
  
          <script src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
          <script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.js' %}"></script>
          {% block js %}{% endblock %}
      </body>
  </html>
  ```

  depart_list.html

  ```html
  {% extends 'layout.html' %}
  
  {% block content %}
      <div class="container">
          <!--按钮-->
          <div style="margin-bottom: 10px">
              <a class="btn btn-success" href="/depart/add/">
                  <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
                  新建部门
              </a>
          </div>
  
          <!--表格 面板-->
          <div class="panel panel-default">
              <!-- Default panel contents -->
              <div class="panel-heading"><font style="vertical-align: inherit;"><font
                      style="vertical-align: inherit;">
                  <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
                  部门列表
              </font></font></div>
  
              <!-- Table -->
              <table class="table">
                  <thead>
                      <tr>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">ID</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">名称</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">操作</font></font></th>
                      </tr>
                  </thead>
                  <tbody>
                      {% for depart in list_depart %}
                          <tr>
                              <th scope="row"><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ depart.id }}</font></font></th>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ depart.title }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">
                                  <a class="btn btn-primary btn-xs" href="/depart/{{ depart.id }}/edit/">编辑</a>
                                  <a class="btn btn-danger btn-xs"
                                     href="/depart/dlt/?nid={{ depart.id }}">删除</a>
                              </font></font></td>
                          </tr>
                      {% endfor %}
                  </tbody>
              </table>
          </div>
  
      </div>
  {% endblock %}
  ```

  depart_add.html

  ```html
  {% extends 'layout.html' %}
  
  {% block content %}
      <div class="container">
          <div class="panel panel-default">
              <div class="panel-heading">
                  <h3 class="panel-title">新建部门</h3>
              </div>
              <div class="panel-body">
  
                  <!--表单-->
                  <form method="post">
                      {% csrf_token %}
                      <div class="form-group">
                          <label>标题</label>
                          <input type="text" class="form-control" placeholder="标题" name="title">
                      </div>
                      <button type="submit" class="btn btn-primary">提 交</button>
                  </form>
  
              </div>
          </div>
      </div>
  {% endblock %}
  ```

  depart_edit.html

  ```html
  {% extends 'layout.html' %}
  
  {% block content %}
      <div class="container">
          <div class="panel panel-default">
              <div class="panel-heading">
                  <h3 class="panel-title">编辑部门</h3>
              </div>
              <div class="panel-body">
  
                  <!--表单-->
                  <form method="post">
                      {% csrf_token %}
                      <div class="form-group">
                          <label>标题</label>
                          <input type="text" class="form-control" placeholder="标题" name="title"
                                 value="{{ row.title }}">
                      </div>
                      <button type="submit" class="btn btn-primary">提 交</button>
                  </form>
  
              </div>
          </div>
      </div>
  {% endblock %}
  ```

  

- 用户管理

  用户列表

  新建用户：user_list链接user_add.html、urls、views)

  删除功能：urls、views) (加入user_list.html 本页面完成)

  编辑页面：urls、views) (携带id：django正则) (传默认值)

  

  user_list.html

  ```html
  {% extends 'layout.html' %}
  
  {% block css %}
      <style>
          .panel {
              margin-bottom: 80px; /* 根据分页控件的高度调整这个值 */
          }
          .fixed-pagination {
              position: fixed;
              bottom: 0;
              left: 50%; /* 把左边位置设置为视窗的50% */
              transform: translateX(-50%); /* 使用transform来移动分页条左边的50%，使其居中 */
              background-color: transparent;
              padding: 10px 0;
          }
      </style>
  {% endblock %}
  
  {% block content %}
      <div class="container">
          <!--按钮-->
          <div style="margin-bottom: 10px">
              <a class="btn btn-success" href="/user/add/">
                  <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
                  新建用户
              </a>
          </div>
  
          <!--表格 面板-->
          <div class="panel panel-default">
              <!-- Default panel contents -->
              <div class="panel-heading"><font style="vertical-align: inherit;"><font
                      style="vertical-align: inherit;">
                  <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
                  用户列表
              </font></font></div>
  
              <!-- Table -->
              <table class="table">
                  <thead>
                      <tr>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">ID</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">姓名</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">密码</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">年龄</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">账户余额</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">入职时间</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">性别</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">所在部门</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">操作</font></font></th>
                      </tr>
                  </thead>
                  <tbody>
                      {% for user in users %}
                          <tr>
                              <th scope="row"><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.id }}</font></font></th>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.name }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.password }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.age }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.account }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.create_time|date:'Y-m-d h:i:s' }}</font></font>
                              </td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.get_gender_display }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.depart.title }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">
                                  <a class="btn btn-primary btn-xs" href="/user/{{ user.id }}/edit/">编辑</a>
                                  <a class="btn btn-danger btn-xs"
                                     href="/user/dlt/?nid={{ user.id }}">删除</a>
                              </font></font></td>
                          </tr>
                      {% endfor %}
                  </tbody>
              </table>
          </div>
  
          <!--分页控件-->
          <nav aria-label="Page navigation" class="fixed-pagination">
              <ul class="pagination">
                  {% if users.has_previous %}
                      <li>
                          <a href="?page=1" aria-label="First">
                              <span aria-hidden="true">&laquo;&laquo;</span>
                          </a>
                      </li>
                      <li>
                          <a href="?page={{ users.previous_page_number }}" aria-label="Previous">
                              <span aria-hidden="true">&laquo;</span>
                          </a>
                      </li>
                  {% else %}
                      <li class="disabled">
                          <a href="#" aria-label="First">
                              <span aria-hidden="true">&laquo;&laquo;</span>
                          </a>
                      </li>
                      <li class="disabled">
                          <a href="#" aria-label="Previous">
                              <span aria-hidden="true">&laquo;</span>
                          </a>
                      </li>
                  {% endif %}
  
                  {% if users.number|add:"-5" > 1 %}
                      <li><a href="?page=1">1</a></li>
                      <li class="disabled"><span>...</span></li>
                  {% endif %}
  
                  {% for i in users.paginator.page_range %}
                      {% if i >= users.number|add:"-5" and i <= users.number|add:"4" %}
                          {% if users.number == i %}
                              <li class="active"><a href="?page={{ i }}">{{ i }}</a></li>
                          {% else %}
                              <li><a href="?page={{ i }}">{{ i }}</a></li>
                          {% endif %}
                      {% endif %}
                  {% endfor %}
  
                  {% if users.number|add:"4" < users.paginator.num_pages %}
                      <li class="disabled"><span>...</span></li>
                      <li><a href="?page={{ users.paginator.num_pages }}">{{ users.paginator.num_pages }}</a></li>
                  {% endif %}
  
                  {% if users.has_next %}
                      <li>
                          <a href="?page={{ users.next_page_number }}" aria-label="Next">
                              <span aria-hidden="true">&raquo;</span>
                          </a>
                      </li>
                      <li>
                          <a href="?page={{ users.paginator.num_pages }}" aria-label="Last">
                              <span aria-hidden="true">&raquo;&raquo;</span>
                          </a>
                      </li>
                  {% else %}
                      <li class="disabled">
                          <a href="#" aria-label="Next">
                              <span aria-hidden="true">&raquo;</span>
                          </a>
                      </li>
                      <li class="disabled">
                          <a href="#" aria-label="Last">
                              <span aria-hidden="true">&raquo;&raquo;</span>
                          </a>
                      </li>
                  {% endif %}
              </ul>
          </nav>
  
      </div>
  {% endblock %}
  ```

  user_add.html

  ```html
  {% extends 'layout.html' %}
  
  {% block css %}
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  {% endblock %}
  
  {% block content %}
      <div class="container">
          <div class="panel panel-default">
              <div class="panel-heading">
                  <h3 class="panel-title">新建用户</h3>
              </div>
              <div class="panel-body">
  
                  <!--表单-->
                  <form method="post">
                      {% csrf_token %}
                      <div class="form-group">
                          <label>姓名</label>
                          <input type="text" class="form-control" placeholder="姓名" name="username">
  
                          <label>密码</label>
                          <div class="input-group">
                              <input type="password" id="passwordInput" class="form-control" placeholder="密码"
                                     name="password">
                              <span class="input-group-btn">
                                  <button class="btn btn-default" type="button" id="togglePassword"><i
                                          class="fa fa-eye"></i></button>
                              </span>
                          </div>
  
                          <label>年龄</label>
                          <input type="number" class="form-control" placeholder="年龄" name="age">
                          <label>账户余额</label>
                          <input type="number" step="0.01" class="form-control" placeholder="账户余额" name="account">
  
                          <!--<label>入职时间</label>
                          <input type="data" class="form-control" placeholder="入职时间" name="create_time">
                          <label>所属部门</label>
                          <input type="text" class="form-control" placeholder="所属部门" name="depart_id">
                          <label>性别</label>
                          <input type="text" class="form-control" placeholder="性别" name="gender">-->
  
                          <label>入职时间</label>
                          <input type="datetime-local" name="create_time" class="form-control">
  
                          <label>所属部门</label>
                          <select name="depart" class="form-control">
                              {% for dept in departments %}
                                  <option value="{{ dept.id }}">{{ dept.title }}</option>
                              {% endfor %}
                          </select>
  
                          <label>性别</label>
                          <div>
                              {% for value, name in gender_choices %}
                                  <label class="radio-inline">
                                      <input type="radio" name="gender" value="{{ value }}"> {{ name }}
                                  </label>
                              {% endfor %}
                          </div>
                      </div>
  
                      <button type="submit" class="btn btn-primary">提 交</button>
                  </form>
  
              </div>
          </div>
      </div>
  {% endblock %}
  
  {% block js %}
      <script>
          document.getElementById('togglePassword').addEventListener('click', function () {
              let passwordInput = document.getElementById('passwordInput');
              if (passwordInput.type === "password") {
                  passwordInput.type = "text";
              } else {
                  passwordInput.type = "password";
              }
          });
      </script>
  {% endblock %}
  ```

  user_edit.html

  ```html
  {% extends 'layout.html' %}
  
  {% block css %}
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
  {% endblock %}
  
  {% block content %}
      <div class="container">
          <div class="panel panel-default">
              <div class="panel-heading">
                  <h3 class="panel-title">编辑用户</h3>
              </div>
              <div class="panel-body">
  
                  <!--表单-->
                  <form method="post">
                      {% csrf_token %}
                      <div class="form-group">
                          <label>姓名</label>
                          <input type="text" class="form-control" placeholder="姓名" name="username"
                                 value="{{ row.name }}">
  
                          <label>密码</label>
                          <div class="input-group">
                              <input type="password" id="passwordInput" class="form-control" placeholder="密码"
                                     name="password" value="{{ row.password }}">
                              <span class="input-group-btn">
                                  <button class="btn btn-default" type="button" id="togglePassword"><i
                                          class="fa fa-eye"></i></button>
                              </span>
                          </div>
  
                          <label>年龄</label>
                          <input type="number" class="form-control" placeholder="年龄" name="age" value="{{ row.age }}">
                          <label>账户余额</label>
                          <input type="number" step="0.01" class="form-control" placeholder="账户余额" name="account"
                                 value="{{ row.account }}">
  
                          <label>入职时间</label>
                          <input type="datetime-local" name="create_time" class="form-control"
                                 value="{{ row.create_time|date:'Y-m-d\TH:i' }}">
  
                          <label>所属部门</label>
                          <select name="depart" class="form-control">
                              {% for dept in departments %}
                                  <option value="{{ dept.id }}" {% if row.depart.id == dept.id %}selected{% endif %}>
                                      {{ dept.title }}
                                  </option>
                              {% endfor %}
                          </select>
  
                          <label>性别</label>
                          <div>
                              {% for value, name in gender_choices %}
                                  <label class="radio-inline">
                                      <input type="radio" name="gender" value="{{ value }}"
                                             {% if row.gender == value %}checked{% endif %}>
                                      {{ name }}
                                  </label>
                              {% endfor %}
                          </div>
  
  
                      </div>
                      <button type="submit" class="btn btn-primary">提 交</button>
                  </form>
  
              </div>
          </div>
      </div>
  {% endblock %}
  
  {% block js %}
      <script>
          document.getElementById('togglePassword').addEventListener('click', function () {
              let passwordInput = document.getElementById('passwordInput');
              if (passwordInput.type === "password") {
                  passwordInput.type = "text";
              } else {
                  passwordInput.type = "password";
              }
          });
      </script>
  {% endblock %}
  ```

  

  

#### django组件 (后续)

- Form组件、ModelForm组件(最方便)

  1 获取用户输入的信息需要校验

  2 遇到错误提示用户

  3 重复代码

  4 关联数据



- Form组件 (单例代码)

  views.py	

  ```python
  class MyForm(Form):
      user = forms.CharField(widget=forms.Input)
      pwd = form.CharFiled(widget=forms.Input)
      email = form.CharFiled(widget=forms.Input)
      account = form.CharFiled(widget=forms.Input)
      create_time = form.CharFiled(widget=forms.Input)
      depart = form.CharFiled(widget=forms.Input)
      gender = form.CharFiled(widget=forms.Input)
  
  
  def user_add(request):
      if request.method == "GET":
          form = MyForm()
          return render(request, 'user_add.html',{"form":form})
  ```

  user_add.html

  ```html
  <form method="post">
      {% for field in form%}
      	{{ field }}
      {% endfor %}
      <!-- <input type="text"  placeholder="姓名" name="user" /> -->
  </form>
  ```

  ```html
  <form method="post">
      {{ form.user }}
      {{ form.pwd }}
      {{ form.email }}
      <!-- <input type="text"  placeholder="姓名" name="user" /> -->
  </form>
  ```

  

- ModelForm组件 (单例代码)

  models.py

  ```python
  class UserInfo(models.Model):
      """ 员工表 """
      name = models.CharField(verbose_name="姓名", max_length=16)
      password = models.CharField(verbose_name="密码", max_length=64)
      age = models.IntegerField(verbose_name="年龄")
      account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
      create_time = models.DateTimeField(verbose_name="入职时间")
      depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
      gender_choices = (
          (1, "男"),
          (2, "女"),
      )
      gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
  ```

  views.py

  ```python
  class MyForm(ModelForm):
      xx = form.CharField*("...")
      class Meta:
          model = UserInfo
          fields = ["name","password","age","xx"]
  
  
  def user_add(request):
      if request.method == "GET":
          form = MyForm()
          return render(request, 'user_add.html',{"form":form})
  ```

  user_add.html

  ```html
  <form method="post">
      {% for field in form%}
      	{{ field }}
      {% endfor %}
      <!-- <input type="text"  placeholder="姓名" name="user" /> -->
  </form>
  ```

  ```html
  <form method="post">
      {{ form.user }}
      {{ form.pwd }}
      {{ form.email }}
      <!-- <input type="text"  placeholder="姓名" name="user" /> -->
  </form>
  ```

   

- 添加用户user_model_form_add

  ModelForm的外键字段展示

  models.py

  ```python
  from django.db import models
  
  
  class Department(models.Model):
      ''' 部门表 '''
      title = models.CharField(verbose_name='标题', max_length=100)
  
      def __str__(self):
          return self.title
  
  
  class UserInfo(models.Model):
      ''' 员工表 '''
      name = models.CharField(verbose_name='姓名', max_length=16)
      password = models.CharField(verbose_name='密码', max_length=64)
      age = models.IntegerField(verbose_name='年龄')
      account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
      create_time = models.DateTimeField(verbose_name='入职时间')
  
      depart = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)
  
      gender_choices = ((1, '男'), (0, '女'))  # 性别不会增减  字节占用少  django约束
      gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
  ```

  

- ModelForm的views函数 (校验+提示)

  views.py

  ```python
  class UserModelForm(ModelForm):
      # 额外加验证
      # name = forms.CharField(min_length=2, label='用户名')
      # password = forms.CharField(label='密码',validators=)  # 正则
  
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
  ```

  ModelForm的html表单 user_model_form_add.html

  ```html
                  <!--表单-->
                  <form method="post" novalidate>
                      {% csrf_token %}
  
                      {% for field in form %}
                          <label>{{ field.label }}</label>
                          {{ field }}
                          <span style="color: red;">{{ field.errors.0 }}</span>
                          <br><br>
                      {% endfor %}
  
                      <button type="submit" class="btn btn-primary">提 交</button>
                  </form>
  ```

  ModelForm的中文错误提示

  settings.py

  ```python
  # LANGUAGE_CODE = "en-us"
  LANGUAGE_CODE = "zh-hans"
  ```

  

- 编辑用户user_model_form_edit

  点击编辑，跳转到编辑页面（将编辑行的ID携带过去）

  编辑页面（默认数据，根据ID获取并设置到页面中）

  提交：错误提示、数据校验、在数据库更新

- ModelForm把默认数据填进去 (之前：在input设置value)

  views.py

  ```python
  def user_model_form_edit(request, nid):
      """ 用户编辑 model form """
      if request.method == 'GET':
          row = UserInfo.objects.filter(id=nid).first()
          form = UserModelForm(instance=row)  # mf 设置默认值
          return render(request, 'user_model_form_edit.html', {'form': form})
  ```

  ModelForm变新增为修改

  views.py

  ```python
  def user_model_form_edit(request, nid):
      """ 用户编辑 model form """
      row = UserInfo.objects.filter(id=nid).first()
      
      if request.method == 'GET':
          form = UserModelForm(instance=row)  # mf 设置默认值
          return render(request, 'user_model_form_edit.html', {'form': form})
      # POST
      form = UserModelForm(data=request.POST, instance=row)  # 变新增为提交
      if form.is_valid():
          form.save()
          return redirect('/user/list/')
      # 不合法数据
      return render(request, 'user_model_form_edit.html', {'form': form})
  ```

  删除用户

  ...



#### 代码集合

- settings.py

  ```python
  # LANGUAGE_CODE = "en-us"
  LANGUAGE_CODE = "zh-hans"
  ```

  

- 表结构

  models.py  (面向对象__str)

  ```python
  from datetime import datetime
  
  from django.db import models
  
  
  class Department(models.Model):
      """ 部门表 """
      title = models.CharField(verbose_name='标题', max_length=100)
  
      def __str__(self):
          return self.title
  
  
  class UserInfo(models.Model):
      """ 员工表 """
      name = models.CharField(verbose_name='姓名', max_length=16)
      password = models.CharField(verbose_name='密码', max_length=64)
      age = models.IntegerField(verbose_name='年龄')
      account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
      create_time = models.DateTimeField(verbose_name='入职时间', default=datetime.now)
  
      depart = models.ForeignKey(verbose_name='部门', to='Department', to_field='id', on_delete=models.CASCADE)
  
      gender_choices = ((1, '男'), (0, '女'))  # 性别不会增减  字节占用少  django约束
      gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
  
  ```

  

- 路由和视图函数

  urls.py

  ```python
  from django.contrib import admin
  from django.urls import path
  
  from app01 import views
  
  urlpatterns = [
      path('admin/', admin.site.urls),
  
      # 部门管理
      path("depart/list/", views.depart_list),
      path("depart/add/", views.depart_add),
      path("depart/dlt/", views.depart_dlt),
      path("depart/<int:nid>/edit/", views.depart_edit),
  
      # 用户管理
      path("user/list/", views.user_list),
      path("user/add/", views.user_add),
      path("user/dlt/", views.user_dlt),
      path("user/<int:nid>/edit/", views.user_edit),
  
      path("user/model/form/add/", views.user_model_form_add),
      path("user/model/form/<int:nid>/edit/", views.user_model_form_edit),
  ]
  ```

  views.py

  ```python
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
  
  ```

  

- 静态文件

  母板

  layout.html

  ```html
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>员工管理系统</title>
          <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
          {% block css %}{% endblock %}
      </head>
  
  
      <body>
          <!--导航栏-->
          <nav class="navbar navbar-default">
              <div class="container">
                  <!-- Brand and toggle get grouped for better mobile display -->
                  <div class="navbar-header">
                      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                              data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                          <span class="sr-only">Toggle navigation</span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                          <span class="icon-bar"></span>
                      </button>
                      <a class="navbar-brand" href="#">员工用户管理系统</a>
                  </div>
  
                  <!-- Collect the nav links, forms, and other content for toggling -->
                  <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                      <ul class="nav navbar-nav">
                          <li><a href="/depart/list/">部门管理</a></li>
                          <li><a href="/user/list/">用户管理</a></li>
                      </ul>
                      <ul class="nav navbar-nav navbar-right">
                          <li><a href="#">登录</a></li>
                          <li class="dropdown">
                              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
                                 aria-haspopup="true" aria-expanded="false">周坚深 <span class="caret"></span></a>
                              <ul class="dropdown-menu">
                                  <li><a href="#">个人资料</a></li>
                                  <li><a href="#">我的信息</a></li>
                                  <li role="separator" class="divider"></li>
                                  <li><a href="#">注销</a></li>
                              </ul>
                          </li>
                      </ul>
                  </div><!-- /.navbar-collapse -->
              </div><!-- /.container-fluid -->
          </nav>
  
          <!--主界面-->
          <div>
              {% block content %}{% endblock %}
          </div>
  
          <script src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
          <script src="{% static 'plugins/bootstrap-3.4.1/js/bootstrap.js' %}"></script>
          {% block js %}{% endblock %}
      </body>
  </html>
  ```

  模板

  user_list2.html

  ```html
  {% extends 'layout.html' %}
  
  {% block css %}
      <style>
          .panel {
              margin-bottom: 80px; /* 根据分页控件的高度调整这个值 */
          }
  
          .fixed-pagination {
              position: fixed;
              bottom: 0;
              left: 50%; /* 把左边位置设置为视窗的50% */
              transform: translateX(-50%); /* 使用transform来移动分页条左边的50%，使其居中 */
              background-color: transparent;
              padding: 10px 0;
          }
      </style>
  {% endblock %}
  
  {% block content %}
      <div class="container">
          <!--按钮-->
          <div style="margin-bottom: 10px">
              <a class="btn btn-success" href="/user/add/">
                  <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
                  新建用户
              </a>
              <a class="btn btn-success" href="/user/model/form/add/">
                  <span class="glyphicon glyphicon-plus-sign" aria-hidden="true"></span>
                  新建用户mf
              </a>
          </div>
  
          <!--表格 面板-->
          <div class="panel panel-default">
              <!-- Default panel contents -->
              <div class="panel-heading"><font style="vertical-align: inherit;"><font
                      style="vertical-align: inherit;">
                  <span class="glyphicon glyphicon-th-list" aria-hidden="true"></span>
                  用户列表
              </font></font></div>
  
              <!-- Table -->
              <table class="table">
                  <thead>
                      <tr>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">ID</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">姓名</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">密码</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">年龄</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">账户余额</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">入职时间</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">性别</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">所在部门</font></font></th>
                          <th><font style="vertical-align: inherit;"><font
                                  style="vertical-align: inherit;">操作</font></font></th>
                      </tr>
                  </thead>
                  <tbody>
                      {% for user in users %}
                          <tr>
                              <th scope="row"><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.id }}</font></font></th>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.name }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.password }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.age }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.account }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.create_time|date:'Y-m-d h:i:s' }}</font></font>
                              </td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.get_gender_display }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">{{ user.depart.title }}</font></font></td>
                              <td><font style="vertical-align: inherit;"><font
                                      style="vertical-align: inherit;">
                                  <a class="btn btn-primary btn-xs" href="/user/{{ user.id }}/edit/">编辑</a>
                                  <a class="btn btn-primary btn-xs" href="/user/model/form/{{ user.id }}/edit/">编辑mf</a>
                                  <a class="btn btn-danger btn-xs"
                                     href="/user/dlt/?nid={{ user.id }}">删除</a>
                              </font></font></td>
                          </tr>
                      {% endfor %}
                  </tbody>
              </table>
          </div>
  
          <!--分页控件-->
          <nav aria-label="Page navigation" class="fixed-pagination">
              <ul class="pagination">
                  {% if users.has_previous %}
                      <li>
                          <a href="?page=1" aria-label="First">
                              <span aria-hidden="true">&laquo;&laquo;</span>
                          </a>
                      </li>
                      <li>
                          <a href="?page={{ users.previous_page_number }}" aria-label="Previous">
                              <span aria-hidden="true">&laquo;</span>
                          </a>
                      </li>
                  {% else %}
                      <li class="disabled">
                          <a href="#" aria-label="First">
                              <span aria-hidden="true">&laquo;&laquo;</span>
                          </a>
                      </li>
                      <li class="disabled">
                          <a href="#" aria-label="Previous">
                              <span aria-hidden="true">&laquo;</span>
                          </a>
                      </li>
                  {% endif %}
  
                  {% if users.number|add:"-5" > 1 %}
                      <li><a href="?page=1">1</a></li>
                      <li class="disabled"><span>...</span></li>
                  {% endif %}
  
                  {% for i in users.paginator.page_range %}
                      {% if i >= users.number|add:"-5" and i <= users.number|add:"4" %}
                          {% if users.number == i %}
                              <li class="active"><a href="?page={{ i }}">{{ i }}</a></li>
                          {% else %}
                              <li><a href="?page={{ i }}">{{ i }}</a></li>
                          {% endif %}
                      {% endif %}
                  {% endfor %}
  
                  {% if users.number|add:"4" < users.paginator.num_pages %}
                      <li class="disabled"><span>...</span></li>
                      <li><a href="?page={{ users.paginator.num_pages }}">{{ users.paginator.num_pages }}</a></li>
                  {% endif %}
  
                  {% if users.has_next %}
                      <li>
                          <a href="?page={{ users.next_page_number }}" aria-label="Next">
                              <span aria-hidden="true">&raquo;</span>
                          </a>
                      </li>
                      <li>
                          <a href="?page={{ users.paginator.num_pages }}" aria-label="Last">
                              <span aria-hidden="true">&raquo;&raquo;</span>
                          </a>
                      </li>
                  {% else %}
                      <li class="disabled">
                          <a href="#" aria-label="Next">
                              <span aria-hidden="true">&raquo;</span>
                          </a>
                      </li>
                      <li class="disabled">
                          <a href="#" aria-label="Last">
                              <span aria-hidden="true">&raquo;&raquo;</span>
                          </a>
                      </li>
                  {% endif %}
              </ul>
          </nav>
  
      </div>
  {% endblock %}
  ```

  user_model_form_add.html

  ```html
  {% extends 'layout.html' %}
  
  {% block content %}
      <div class="container">
          <div class="panel panel-default">
              <div class="panel-heading">
                  <h3 class="panel-title">新建用户</h3>
              </div>
              <div class="panel-body">
  
                  <!--表单-->
                  <form method="post" novalidate>
                      {% csrf_token %}
  
                      {% for field in form %}
                          <label>{{ field.label }}</label>
                          {{ field }}
                          <span style="color: red;">{{ field.errors.0 }}</span>
                          <br><br>
                      {% endfor %}
  
                      <button type="submit" class="btn btn-primary">提 交</button>
                  </form>
  
              </div>
          </div>
      </div>
  {% endblock %}
  ```

  user_model_form_edit.html

  ```html
  {% extends 'layout.html' %}
  
  {% block content %}
      <div class="container">
          <div class="panel panel-default">
              <div class="panel-heading">
                  <h3 class="panel-title">编辑用户</h3>
              </div>
              <div class="panel-body">
  
                  <!--表单-->
                  <form method="post" novalidate>
                      {% csrf_token %}
  
                      {% for field in form %}
                          <label>{{ field.label }}</label>
                          {{ field }}
                          <span style="color: red;">{{ field.errors.0 }}</span>
                          <br><br>
                      {% endfor %}
  
                      <button type="submit" class="btn btn-primary">提 交</button>
                  </form>
  
              </div>
          </div>
      </div>
  {% endblock %}
  ```

  



### 靓号管理










