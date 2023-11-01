from logging import Logger

from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01 import models


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    user = request.POST.get("username")
    pwd = request.POST.get("password")
    print(user)
    print(pwd)
    user_object = models.Admin.objects.filter(username=user, password=pwd).first()
    print(user_object)
    if user_object:
        # 生成随机字符串 + 返回用户浏览器 + 将数据写入session
        request.session['user_info'] = {'id': user_object.id, 'username': user_object.username}
        # ynpgqtdd2kuj93x7nma09m4f7c0pnagc
        return redirect('/depart/list/')
    else:
        return render(request, "login.html", {"error": "Invalid username or password"})


def depart_list(request):
    user_info = request.session.get("user_info")
    if not user_info:
        return redirect('/login/')
    return HttpResponse("部门列表")

def asset_list(request):
    user_info = request.session.get("user_info")
    if not user_info:
        return redirect('/login/')
    return HttpResponse("工司资产信息")