import copy

from django.utils.safestring import mark_safe


class Pagination(object):
    """ 
    自定义的分类组件

    在视图函数：
    # 1 根据情况筛选数据
    queryset = PrettyNum.objects.filter(**data_dict).order_by('-level')  # 搜索完的数据
    # 2 实例化分页对象
    page_object = Pagination(request, queryset)  # page_size=20
    context = {
        'list_xxxxx': page_object.page_queryset,  # 分完页的数据
        'page_string': page_object.html()  # 页码
    }

    在html：
        <ul class="pagination">
            {{ page_string }}
        </ul>
    """

    def __init__(self, request, queryset, page_size=20, page_param='page', plus=5):
        """
        @param request: 请求对象
        @param queryset: 符合条件的数据 (尚未分页处理)
        @param page_size: 每页显示多少条数据
        @param page_param: 在url中传递发获取分页的参数  ?page=4
        @param plus: 显示当前页的前n后n
        """

        # url &
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param  # 当前要新加的

        # 获取当前页  每页多少个
        page = request.GET.get(page_param, '1')
        self.page = int(page) if page.isdecimal() else 1
        self.page_size = page_size
        # 起始结束
        self.start = (self.page - 1) * page_size
        self.end = self.page * page_size
        # 所有页的数据
        self.page_queryset = queryset[self.start:self.end]
        # 总页码
        total_count = queryset.count()  # 数据总条数
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        # 前5后5
        self.plus = plus

    def html(self):
        # 选择当前页的前五后五
        if self.total_page_count <= 2 * self.plus + 1:  # 当数据较少
            left_page = 1
            right_page = self.total_page_count
        else:  # 当数据较多
            left_page = self.page - self.plus
            right_page = self.page + self.plus
            if self.page <= self.plus:  # 当前页小于前5
                left_page = 1
            if self.page >= self.total_page_count - self.plus:  # 当前页大于后5
                right_page = self.total_page_count

        page_str_list = []
        # url &
        self.query_dict.setlist(self.page_param, [1])  # 在原来的条件上 加新的
        # 首页
        page_str_list.append(f'<li><a href="?{self.query_dict.urlencode()}">首页</a></li>')
        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])  # 在原来的条件上 加新的
            prev = f'<li><a href="?{self.query_dict.urlencode()}">上一页</a></li>'
        else:
            self.query_dict.setlist(self.page_param, [1])  # 在原来的条件上 加新的
            prev = f'<li><a href="?{self.query_dict.urlencode()}">上一页</a></li>'
        page_str_list.append(prev)
        # 前五后五
        for i in range(left_page, right_page + 1):
            if i == self.page:  # 当前页 标识
                self.query_dict.setlist(self.page_param, [i])  # 在原来的条件上 加新的
                ele = f'<li class="active"><a href="?{self.query_dict.urlencode()}">{i}</a></li>'
            else:
                self.query_dict.setlist(self.page_param, [i])  # 在原来的条件上 加新的
                ele = f'<li><a href="?{self.query_dict.urlencode()}">{i}</a></li>'
            page_str_list.append(ele)
        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])  # 在原来的条件上 加新的
            prev = f'<li><a href="?{self.query_dict.urlencode()}">下一页</a></li>'
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])  # 在原来的条件上 加新的
            prev = f'<li><a href="?{self.query_dict.urlencode()}">下一页</a></li>'
        page_str_list.append(prev)
        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])  # 在原来的条件上 加新的
        page_str_list.append(f'<li><a href="?{self.query_dict.urlencode()}">尾页</a></li>')

        # 查询页
        search_string = """
         <li>
            <form method="get" style="float: left; margin-left: -1px">
                <input type="text" class="form-control" placeholder="页码" name="page"
                       style="position: relative; float: left; display: inline-block; width: 80px; border-radius: 0;">
                <button class="btn btn-default" type="submit"><font style="vertical-align: inherit;"><font
                        style="vertical-align: inherit;">跳转</font></font></button>
            </form>
        </li>
        """  # ajax
        page_str_list.append(search_string)

        page_string = mark_safe(''.join(page_str_list))  # 标记安全 html
        return page_string
