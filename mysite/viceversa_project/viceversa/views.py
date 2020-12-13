from django.http import HttpResponse
from django.shortcuts import render
from  django.core.paginator import Paginator

def about(request):
    objects = ['table1', 'dog2', 'cat3', 'meat4', 'fish5', 'bird6', 'fox7', 'chair8']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    #return HttpResponse("Hello people")
    return render(request, 'news/test.html', {'page_obj': page_obj})


def home(request):
    return render(request, 'home.html', {"gosha": request})

def reverse(request):
    text = request.GET['usertext']
    words = 0
    pos = 'out'
    for letter in text:
        # Если очередной символ не пробел, а флаг в значении "вне слова",
        # то значит начинается новое слово.
        if letter != ' ' and pos == 'out':
            # Поэтому надо увеличить счетчик слов на 1,
            words += 1
            # а флаг поменять на значение "внутри слова".
            pos = 'in'
        # Если очередной символ пробел,
        elif letter == ' ':
            # то следует установить флаг в значение "вне слова".
            pos = 'out'
    kol = words
    print(kol)
    get_text = text[::-1]

    return render(request, 'reverse.html', {'user_text': text, 'reverse_text': get_text, 'kol': kol})
