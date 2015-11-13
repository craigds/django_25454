from django.db import models, connection
from django.contrib.postgres.fields import HStoreField


# Force connection init before models are loaded.
# Causes https://code.djangoproject.com/ticket/25454#comment:2
with connection.cursor() as c:
    c.execute("select 1")


class MyModel(models.Model):
    h = HStoreField()
