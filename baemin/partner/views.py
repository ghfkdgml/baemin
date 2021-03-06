from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PartnerForm,MenuForm
from .models import Menu
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    ctx={}
    if request.method=="GET":
        partner_form=PartnerForm()
        ctx.update({"form":partner_form})
    elif request.method=="POST":
        partner_form=PartnerForm(request.POST)
        if partner_form.is_valid():
            partner=partner_form.save(commit=False)
            partner.user=request.user
            partner.save()
            return redirect("/partner")
        else:
            ctx.update({"form":partner_form})
    return render(request,"index.html",ctx)

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
                return redirect("/partner")
        else:
            messages.info(request,"user not exists!")
            return redirect("/partner/login")


    ctx={}
    return render(request,"login.html",ctx)

def logout(request):
    authlogout(request)
    return redirect("/partner")

def signup(request):
    if request.method=="GET":
        pass
    elif request.method=="POST":
         username=request.POST.get('Id')
         email=request.POST.get('Email')
         password=request.POST.get('Password')
         try:
             user=User.objects.create_user(username=username,email=email,password=password)
             messages.info(request,"complete!")
         except:
             messages.error(request,"exist!")
         # print(username,email,password)
    ctx={

    }
    return render(request,"signup.html",ctx)
@login_required(login_url="/partner/login")
def menu(request,menu_alter):
    ctx={}
    # print(menu_alter.split('_')[0])
    if  request.user.is_anonymous or request.user.partner is None:
        return redirect("/partner")
    if request.method=="GET":
        if  menu_alter.split('_')[0]=='alter':
            menu=Menu.objects.get(id=int(menu_alter.split('_')[1]))
            form= MenuForm(instance=menu)
            ctx.update({"form":form,"edit":"yes"})
        else:
            form= MenuForm()
            ctx.update({"form":form})
    elif request.method=="POST":
        if  menu_alter.split('_')[0]=='alter':
            menu=Menu.objects.get(id=int(menu_alter.split('_')[1]))
            print(menu.price)
            form= MenuForm(request.POST,request.FILES,instance=menu)
            if form.is_valid():
                menu=form.save(commit=False)
                menu.partner=request.user.partner
                menu.save()
                return redirect("/partner/menu_list")
            else:
                ctx.update({"form":form,"edit":"yes"})
        else:
            form= MenuForm(request.POST,request.FILES)
            if form.is_valid():
                menu=form.save(commit=False)
                menu.partner=request.user.partner
                menu.save()
                return redirect("/partner/menu_list")
            else:
                ctx.update({"form":form})
    return render(request,"menu.html",ctx)
    
@login_required(login_url="/partner/login/")
def menu_list(request):
    ctx={}
    if  request.user.is_anonymous or request.user.partner is None:
        return redirect("/partner")
    menu_list=Menu.objects.filter(partner=request.user.partner)
    ctx.update({"menu_list":menu_list})
    return render(request,"menu_list.html",ctx)

@login_required(login_url="/partner/login/")
def menu_detail(request,menu_id):
    ctx={}
    menu=Menu.objects.get(id=menu_id)
    ctx.update({"menu":menu})
    return render(request,"menu_detail.html",ctx)

@login_required(login_url="/partner/login/")
def menu_delete(request,menu_del):
    ctx={}
    menu=Menu.objects.get(id=menu_del)
    menu.delete()
    return redirect("/partner/menu_list/")
    # return render(request,"menu_detail.html",ctx)

def edit_info(request):
    ctx={}
    # partner_form=PartnerForm(instance=request.user.partner)
    # ctx.update({"form":partner_form})
    if request.method=="GET":
        partner_form=PartnerForm(instance=request.user.partner)
        ctx.update({"form":partner_form})
    elif request.method=="POST":
        partner_form=PartnerForm(request.POST,instance=request.user.partner)
        if partner_form.is_valid():
            partner=partner_form.save(commit=False)
            partner.user=request.user
            partner.save()
            return redirect("/partner")
    return render(request,"edit_info.html",ctx)
