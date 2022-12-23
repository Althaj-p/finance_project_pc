# Generated by Django 3.2.13 on 2022-12-03 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('broker_app', '0008_alter_profit_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='profit_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(null=True)),
                ('date_added', models.DateField(null=True)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='broker_app.projects')),
            ],
        ),
    ]
