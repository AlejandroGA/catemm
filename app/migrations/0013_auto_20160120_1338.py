# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160119_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segundoregistro',
            name='tarjeta_entregada',
            field=models.BooleanField(default=models.CharField(max_length=50)),
        ),
    ]
