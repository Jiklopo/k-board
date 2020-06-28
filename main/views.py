from django.shortcuts import render, get_object_or_404
from main.models import Add, UserInfo


def index(request):
    return render(request, 'index.html')


def adds(request):
    adds = Add.objects.all().order_by('-created')[:10]
    return render(request, 'adds/adds.html', {'adds': adds})


def add(request, add_id):
    add = get_object_or_404(Add, pk=add_id)
    return render(request, 'adds/add.html', {'add': add})


def user(request, user_id):
    user = get_object_or_404(Add, pk=user_id)
    return render(request, 'users/user_info.html', {'user': user})
