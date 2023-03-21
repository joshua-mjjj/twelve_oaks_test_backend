# Generated by Django 3.2.8 on 2022-12-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20221213_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clinicaldata',
            options={'verbose_name': 'Clinical Data', 'verbose_name_plural': 'Clinical Data'},
        ),
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'verbose_name': 'Diagnosis', 'verbose_name_plural': 'Diagnosis'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
        migrations.AlterModelOptions(
            name='ultrasoundimage',
            options={'verbose_name': 'Ultrasound Image', 'verbose_name_plural': 'Ultrasound Images'},
        ),
        migrations.AddField(
            model_name='patient',
            name='first_name',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='patient',
            name='last_name',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
    ]
