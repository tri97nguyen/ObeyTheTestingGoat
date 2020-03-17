from django.shortcuts import render,redirect
from django.http import HttpResponse
from list.models import Item,List


def home_page(request):
    return render(request,'home.html')

def view_list(request):
    context = {'items':Item.objects.all()}
    return render(request,'list.html',context)

def new_list(request):
    if request.method == 'POST':
        list_ = List()
        list_.save()
        Item.objects.create(text=request.POST.get('item_text',''),listy = list_)
        return redirect('/list/unique-list-url-for-each-user')
     
