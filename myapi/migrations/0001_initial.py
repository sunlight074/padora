# Generated by Django 4.2.1 on 2023-06-07 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EVENT_LOG',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sid', models.CharField(max_length=500)),
                ('search_name', models.CharField(max_length=150)),
                ('app', models.CharField(max_length=150)),
                ('owner', models.CharField(max_length=150)),
                ('results_link', models.CharField(max_length=150)),
                ('results', models.CharField(max_length=500)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='USERS',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MANAGE_TICKET',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_attack', models.CharField(max_length=36)),
                ('severity_id', models.IntegerField()),
                ('severity_name', models.CharField(max_length=36)),
                ('status', models.IntegerField(default=1)),
                ('description', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('assignee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee_report', to='myapi.users')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporter_report', to='myapi.users')),
            ],
        ),
    ]
