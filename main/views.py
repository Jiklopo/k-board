from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse
from main.models import Add, UserInfo
from main.forms import AddForm


def index(request):
    return render(request, 'index.html')


def adds(request):
    adds = Add.objects.all().order_by('-created')[:10]
    return render(request, 'adds/adds.html', {'adds': adds})


def add(request, add_id):
    add = get_object_or_404(Add, pk=add_id)
    return render(request, 'adds/add.html', {'add': add})


def add_form(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            add = Add(user_id=request.user.id, **form.cleaned_data)
            add.save()
            return HttpResponseRedirect(reverse('main:add_detail', args=(add.id,)))
        print(form.errors)
    else:
        form = AddForm()
    return render(request, 'adds/form.html', {'form': form})


class LoginView(DjangoLoginView):
    pass




def user(request, user_id):
    user = get_object_or_404(Add, pk=user_id)
    return render(request, 'users/user_info.html', {'user': user})
