# -*- coding:utf-8 -*-
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from  .data_process import data_analysis

context = {}

@login_required
def index(request):
    return render(request, 'Visualization/analysis_form.html', context)

@login_required
@csrf_exempt
def analysis(request):
    if request.method=='GET':
        return render(request, 'Visualization/analysis_form.html', context)
    elif request.method=='POST' and request.POST:
        data_form = request.POST
        res = data_analysis(data_form)
        context.update(res)
        return render(request, 'Visualization/analysis_viz.html',context)

@csrf_exempt
def logon(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember = request.POST.get('remember_me', False)
        user = auth.authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                return redirect(request.GET.get('next', reverse('Visualization:analysis')))
            else:
                msg = '用户已删除'
        else:
            msg = '错误的用户名或密码'
        context['error'] = msg
        return render(request, 'Visualization/logon.html', context)
    else:
        context['error'] = False
        context['next'] = request.GET.get('next', reverse('Visualization:analysis'))
        return render(request, 'Visualization/logon.html', context)


@csrf_exempt
def register(request):
   if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirmation']
        msg = ""
        if password!=password_confirm:
            msg = "注册失败，两次输入密码不一致，请检查您的输入信息后重新注册。"
            context['mark'] = 0
            context['msg'] = msg
            return render(request, 'Visualization/success.html', context)
        try:
            user = User.objects.create_user(username,email,password)####
            user.is_staff = True
            user.save()
        except Exception,e:
            msg = "注册失败，注册过程中发生了一个异常。原因可能是：用户名重复，请重新注册。"
            context['msg'] = msg
            context['mark'] = 0
            return render(request, 'Visualization/success.html', context)
        msg = "注册成功，感谢您的注册，欢迎使用新华网无人机可视化系统。"
        context['msg'] = msg
        context['mark'] = 1
        return render(request, 'Visualization/success.html', context)
   else:
       return render(request, 'Visualization/register.html', context)

def logout(request):
    auth.logout(request)
    return redirect('Visualization:logon')