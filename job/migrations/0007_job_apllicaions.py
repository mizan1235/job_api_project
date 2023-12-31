# Generated by Django 4.2.3 on 2023-12-16 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_details_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_apllicaions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='rahul123', max_length=40)),
                ('job_id', models.IntegerField(default='3')),
                ('name', models.CharField(default='rahul', max_length=50)),
                ('father_name', models.CharField(default='rahul', max_length=40)),
                ('mother_name', models.CharField(default='rahul', max_length=40)),
                ('DOB', models.CharField(default='today', max_length=20)),
                ('email', models.EmailField(default='rahul@gamil.com', max_length=30)),
                ('address', models.CharField(default='Your Default Address', max_length=150)),
                ('hometown', models.CharField(default='new work', max_length=20)),
                ('pin', models.IntegerField(default='781316')),
                ('experience', models.CharField(default='rahul', max_length=300)),
                ('resume', models.ImageField(default=None, max_length=250, null=True, upload_to='resume/')),
            ],
        ),
    ]
