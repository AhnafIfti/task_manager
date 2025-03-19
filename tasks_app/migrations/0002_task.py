# Generated by Django 4.2.20 on 2025-03-19 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'In Progress'), (3, 'Completed')])),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks_app.category')),
            ],
        ),
    ]
