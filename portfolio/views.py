# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .signals import test_signal
from django.contrib.auth.models import User

from django.views.generic import FormView
# Create your views here.

def testview(request):
    if request.method=='GET':
        test_signal.send(sender=User)
        return HttpResponse('success')