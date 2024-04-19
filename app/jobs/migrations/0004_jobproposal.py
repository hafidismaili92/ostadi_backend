# Generated by Django 3.2.24 on 2024-04-15 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profils', '0001_initial'),
        ('jobs', '0003_alter_jobpost_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobpost')),
                ('proposed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profils.professor')),
            ],
        ),
    ]