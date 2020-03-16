from django.shortcuts import render,redirect
from django.http import HttpResponse
from list.models import Item


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST.get('item_text', '')
        Item.objects.create(text=new_item_text)
        return redirect('/')
    else:
        new_item_text = ''
    context = {'items': Item.objects.all()}
    return render(request,'home.html',context)
