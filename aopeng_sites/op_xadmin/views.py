from django.shortcuts import render
from django.views import generic
from .models import goods, goodsInfo
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# class OrderDetailView(generic.DetailView):
#     model = orderInfo
#     template_name = ''

    # def get_queryset(self):
    #     return orderInfo.objects.filter(orderInfo.(orderList.order_id)=1)

