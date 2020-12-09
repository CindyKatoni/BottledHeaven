# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Item

# Create your views here.
def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "item_list.html", context)