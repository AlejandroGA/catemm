# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20160120_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segundoregistro',
            name='tarjeta_entregada',
            field=models.BooleanField(),
        ),
    ]
