import re

from django.http import HttpResponse
from django.shortcuts import render
from django import forms


class UserForm(forms.Form):
    SendMeText = forms.CharField()


def index_page(request):
    print("\xAB")  # это «
    print("\xBB")  # это »
    print("\x22")  # это "
    if request.method == 'POST':
        s1 = request.POST.get('SendMeText')
        origin = s1[:]
        changed = re.sub(
            pattern=r'"$|" +',
            repl="\xBB ",
            string=re.sub(
                pattern=r'^"| +"',
                repl=" \xAB",
                string=origin
            ).strip(" ")
        ).strip(" ")

        return HttpResponse(f'<h1>Ты ввел: {origin}</h1><h1>Отредактированный текст: {changed}</h1>')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})
