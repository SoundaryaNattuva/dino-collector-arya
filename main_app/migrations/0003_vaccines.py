# Generated by Django 4.2.10 on 2024-03-01 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_dino_height_alter_dino_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('shot', models.CharField(choices=[('F', 'Flu'), ('P', 'Parvovirus'), ('R', 'Rotavirus'), ('T', 'Tetanus'), ('M', 'Measles')], default='F', max_length=1)),
                ('dino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dino')),
            ],
        ),
    ]
