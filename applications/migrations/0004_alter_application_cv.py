# Generated by Django 3.2.8 on 2022-06-22 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_alter_application_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='cv',
            field=models.CharField(max_length=244),
        ),
    ]