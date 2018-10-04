from django.shortcuts import render
from partner.models import Partner
# Create your views here.
def index(request):
    ctx={}
    partner_list=Partner.objects.all()
    ctx.update({
        "partner_list":partner_list,
    })
    return render(request,"main.html",ctx)
