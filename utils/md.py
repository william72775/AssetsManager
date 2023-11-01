from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

class DemoMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 无需登录的地址，放行
        if request.path_info == '/login/':
            return
        # 获取用户session信息
        user_info = request.session.get('user_info')
        # 有值，比送到hi已经发让路，继续
        if user_info:
            return
        # 无值=None
        return redirect('/login/')


    def process_response(self, request, response):
        return response
