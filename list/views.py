from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from list.models import Item,List


def home_page(request):
    return render(request,'home.html')

def view_list(request,list_id):
    # list_ = List.objects.get(id=list_id)
    list_ = get_object_or_404(List,id=list_id)
    # items = Item.objects.filter(listy=list_)
    # context = {'items':items,'list':list_}
    context = {'list':list_}
    return render(request,'list.html',context)

def new_list(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        Item.objects.create(text=request.POST.get('item_text',''),listy = list_)
        return redirect(f'/list/{list_.id}/')

def add_item(request,list_id):
    if request.method == 'POST':
        # list_ = get_object_or_404(List,id = list_id)
        list_= List.objects.get(id=list_id)
        item = Item.objects.create(text=request.POST.get('item_text', ''), listy=list_)
        return redirect(f'/list/{list_.id}/')
