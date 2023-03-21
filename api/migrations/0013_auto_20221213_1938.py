# Generated by Django 3.2.8 on 2022-12-13 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20221124_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signOrSymptom', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=52)),
                ('diagnosisNotes', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
                ('occupation', models.CharField(choices=[('PF', 'Peasant farmer'), ('E', 'employed'), ('NE', 'non-employed')], default='NE', max_length=2)),
                ('smokingStatus', models.CharField(choices=[('S', 'smoker'), ('ES', 'ex-smoker'), ('NS', 'smoker')], default='NS', max_length=2)),
                ('district', models.CharField(max_length=20)),
                ('subcounty', models.CharField(max_length=15)),
                ('parish', models.CharField(max_length=15)),
                ('village', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('signOrSymptom', models.ManyToManyField(to='api.ClinicalData')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='user',
            name='other_name',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Sonographer', 'Sonographer')], max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=32, null=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.CreateModel(
            name='UltrasoundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/Ultrasoundimages')),
                ('hemithorax', models.CharField(choices=[('R', 'right'), ('L', 'left')], default='', max_length=2)),
                ('lungzone', models.CharField(choices=[('U', 'upper'), ('M', 'middle'), ('L', 'lower')], default='', max_length=10)),
                ('location', models.CharField(choices=[('P', 'posterior'), ('AN', 'anterior'), ('AU', 'auxillary')], default='', max_length=10)),
                ('diagnosisId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.diagnosis')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.patient')),
            ],
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.patient'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='sonographerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]