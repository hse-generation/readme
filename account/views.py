from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Users  # импортируем нашу модель Users, по сути нашу табличку
from django.http import HttpResponse, HttpResponseRedirect


def index(request):

    if 'user_id' not in request.session: # если пользователь не авторизован, отправляем на страницу входа
        return redirect('login')

    data = {}  # дата (данные), которая отправляется в view
    if 'save_account_info' in request.POST:  # проверяем была ли нажата кнопочка с name = save_account_info в post запросе
        info = request.POST
        info_pic = AccountForm(request.POST, request.FILES)
        if info_pic.is_valid():
            info_pic.save()
        profile_picture = Users.objects.latest('id').profile_picture
        Users.objects.filter(id=request.session['user_id']).update(name=info['name'],
                                                                   last_name=info['last_name'],
                                                                   about=info['about'],
                                                                   birthdate=info['birthdate'],
                                                                   email=info['email'],
                                                                   profile_picture=profile_picture)
        return redirect("account")

    user = Users.objects.filter(
        id=request.session['user_id']).values()  # берем из accounts вссех юзеров с id равный id пользака из сессии
    form = AccountForm(data=user[0])  # указываем в data значение из базы, чтобы автоматом выставлялись в поля
    data['form'] = form
    return render(request, 'account/index.html', data)
