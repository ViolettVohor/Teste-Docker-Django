from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList
from .forms import NewList

def index(response):
    return render(response, "main/home.html", {})

def lists(response):
    return render(response, "main/lists.html", {})

def lista(response, id):
    lista = ToDoList.objects.get(id=id)

    if lista in response.user.todolist.all():
        if response.method == "POST":
            if response.POST.get("save"):
                for item in lista.item_set.all():
                    if response.POST.get('c' + str(item.id)):
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("itemText")
                if len(txt) > 2:
                    lista.item_set.create(text=txt, complete=False)
                else:
                    print('invalid')
        

        return render(response, "main/list.html", {"list": lista})
    return render(response, "main/lists.html", {})

def create(response):
    if response.method == "POST":
        form = NewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            return HttpResponseRedirect(f'/{t.id}')

    else:
        form = NewList()
    return render(response, "main/create.html", {"form":form})