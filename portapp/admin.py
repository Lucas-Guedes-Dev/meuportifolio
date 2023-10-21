from django.contrib import admin
from django.db import models as md
from . import models

for model_name in dir(models):
    model = getattr(models, model_name)
    if isinstance(model, type) and issubclass(model, md.Model):
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass