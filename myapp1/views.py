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
        s1 = s1.split()
        for index, word in enumerate(origin.split()):
            if word.startswith('"'):
                s1[index] = s1[index].replace('"', '«', 1)
            if word.endswith('"'):
                s1[index] = s1[index].replace('"', '»', 1)
        return HttpResponse(f'<h1>Ты ввел: {origin}</h1><h1>Отредактированный текст: {" ".join(s1)}</h1>')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})
