#!/usr/bin/env python
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = "myproject.settings"

import django
from django.db import connection

from myapp.models import MyModel


django.setup()

if '--be-okay' not in sys.argv:
    # Force connection init before models are loaded.
    # Causes https://code.djangoproject.com/ticket/25454#comment:2
    with connection.cursor() as c:
        c.execute("select 1")

if '--create-with-string' in sys.argv:
    h = '"a" => "b"'
else:
    h = {'a': 'b'}

print("Creating instance with h=%r" % h)
m = MyModel.objects.create(h=h)

print("Created instance %d" % m.pk)

m = MyModel.objects.get(pk=m.pk)
print("Fetched instance, now m.h == %r" % m.h)
