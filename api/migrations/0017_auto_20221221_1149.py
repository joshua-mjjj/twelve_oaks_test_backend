# Generated by Django 3.2.8 on 2022-12-21 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20221221_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='patientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.patient'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='sonographerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ultrasoundimage',
            name='diagnosisId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.diagnosis'),
        ),
        migrations.AlterField(
            model_name='ultrasoundimage',
            name='patientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.patient'),
        ),
    ]
