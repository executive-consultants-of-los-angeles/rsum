#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.shortcuts import render

import json
import models

# Create your views here.

def index(request):
    cv_i = models.CV(id=1)
    cv_i.check_sections()

    cv = cv_i.get_cv()

    context = {
        'cv': cv 
    }

    return render(request, 'home/index.html', context)