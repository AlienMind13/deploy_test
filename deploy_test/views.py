from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from deploy_test.models import Picture


def index(request):
    return render(request, 'deploy_test/index.html')


def show_pic(request, pic_id):
    try:
        current_pic = Picture.objects.get(pk=pic_id)
    except Picture.DoesNotExist:
        raise Http404('Picture does not exist')

    return render(request, 'deploy_test/pic.html', {'pic': current_pic})


def show_all(request):
    pics = Picture.objects.all()
    return render(request, 'deploy_test/pic_list.html', {'pic_list': pics})
