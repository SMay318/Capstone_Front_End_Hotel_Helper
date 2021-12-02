# Generated by Django 3.2.8 on 2021-12-02 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('category', models.CharField(max_length=50)),
                ('severity_rating', models.IntegerField(default=0)),
                ('status_pending', models.BooleanField(default=False)),
                ('status_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]