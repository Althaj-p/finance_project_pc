# Generated by Django 3.2.13 on 2022-12-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker_app', '0013_alter_projects_share'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='investor_name',
        ),
        migrations.AddField(
            model_name='projects',
            name='investor_name',
            field=models.ManyToManyField(null=True, to='broker_app.investors'),
        ),
    ]