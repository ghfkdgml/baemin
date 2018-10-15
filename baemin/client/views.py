from django.shortcuts import render
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from partner.models import Partner,Menu
from .models import Client,Order,OrderItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ClientForm

@login_required(login_url="/client/login")
def index(request):
    ctx={}
    # partner_list=Partner.objects.all()
    # ctx.update({
    #     "partner_list":partner_list,
    # })
    # if request.user:
    #     client_list=request.user
    #     ctx.update({"client_list":client_list})
    #     print(client_list)
    if request.method=="GET":
        client_form=ClientForm()
        ctx.update({"form":client_form})
    elif request.method=="POST":
        client_form=ClientForm(request.POST)
        if client_form.is_valid():
            client=client_form.save(commit=False)
            client.user=request.user
            client.save()
            return redirect("/client")
        else:
            ctx.update({"form":client_form})
    # print(request.user)
    return render(request,"main.html",ctx)

def base(request):
    ctx={}
    return render(request,"home.html",ctx)

def login(request):
    if request.method=="GET":
        pass
    elif request.method=="POST":
        username=request.POST.get('Id')
        password=request.POST.get('Password')
        remember=request.POST.get('remember')
        user=authenticate(username=username,password=password)
        if user is not None:
            authlogin(request,user)
            # return HttpResponseRedirect("/")
            next_value=request.GET.get("next")
            if next_value:
                return redirect(next_value)
            else:
                return redirect("/")
        else:
            messages.info(request,"user not exists!")
            return redirect("/client/login")
    ctx={}
    return render(request,"login.html",ctx)

def logout(request):
    authlogout(request)
    return redirect("/client")

def menu(request):
    partner=Partner.objects.all()
    ctx={
        "partner":partner,
    }
    return render(request,"home.html",ctx)

def menu_list(request,name):
    ctx={}
    # if  request.user.is_anonymous or request.user.partner is None:
    #     return redirect("/partner")
    partner=Partner.objects.get(name=name)
    a=Menu.objects.filter(partner=partner)
    if request.method=="GET":
        ctx.update({"menu_list":a,"client":True})
    elif request.method=="POST":
        # menu_dict={}
        order=Order.objects.create(
            client=request.user.client,
            address="test",
        )
        for menu in a:
            menu_count=request.POST.get(str(menu.id))
            # if int(menu_count)>0:
            #     menu_dict.update({str(menu.id):menu_count})
            if int(menu_count)>0:
                item=OrderItem.objects.create(
                    order=order,
                    menu=menu,
                    count=menu_count
                )
                # order.items.add(menu)
        return redirect("/")

    # print(a.price)
    # menu_list=Menu.objects.filter(partner=name)
    # ctx.update({"menu_list":menu_list})
    return render(request,"client_menu.html",ctx)

def order_check(request):
    ctx={}
    if request.user.client:
        # print(request.user.client)
        try:
            orderlist=[]
            username=request.user.client
            userlist=Order.objects.filter(client=username)
            for user in userlist:
                menulist=OrderItem.objects.filter(order=user)
                print(menulist)
                orderlist.append(list(menulist))
            print(orderlist)
            # order=Order.objects.filter(client=username)
            # for user in userlist:
            #     menu_list=OrderItem.objects.filter(order=user)
            #     orderlist.append(menu_list)
            #     print(orderlist)
            ctx.update({"menu_list":orderlist})
        except Exception as e:
            print(e)
            pass
    return render(request,"ordercheck.html",ctx)

def delete_order(request):
    ctx={}
    id=request.GET['id']
    if id:
        order=OrderItem.objects.get(id=id)
        order.delete()
        return redirect("/client/orderlist")
    else:
        msg="delete order failed!"
        ctx.update({"msg":msg})
        return render(request,"ordercheck.html",ctx)
