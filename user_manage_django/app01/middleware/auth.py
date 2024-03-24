from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        """ 拦截未登录 """
        if request.path_info in ['/login/', '/image/code/']:
            return  # 未登录能访问的

        info_dict = request.session.get('info')
        if info_dict:
            return  # 有登录信息的通过

        return redirect('/login/')  # 没登陆信息的去登录页面
