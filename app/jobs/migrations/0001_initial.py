# Generated by Django 3.2.23 on 2024-02-26 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.duration')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profils.student')),
            ],
        ),
    ]