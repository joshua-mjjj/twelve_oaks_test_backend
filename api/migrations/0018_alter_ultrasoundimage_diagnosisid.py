# Generated by Django 3.2.8 on 2022-12-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20221221_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ultrasoundimage',
            name='diagnosisId',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]