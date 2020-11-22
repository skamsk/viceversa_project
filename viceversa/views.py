from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse("Hello people")


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
