# Generated by Django 3.2.8 on 2022-11-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_recruitmentagency_registration_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_field', models.CharField(max_length=52, unique=True)),
            ],
            options={
                'verbose_name': 'Test Model',
                'verbose_name_plural': 'Test Models',
            },
        ),
        migrations.RemoveField(
            model_name='worker',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='home_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='occupation',
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Radiographer', 'Radiographer')], max_length=32),
        ),
        migrations.DeleteModel(
            name='RecruitmentAgency',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
