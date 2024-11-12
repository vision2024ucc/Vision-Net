# Generated by Django 5.1.3 on 2024-11-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=200)),
                ('segundo_nombre', models.CharField(max_length=200)),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('contraseña', models.CharField(max_length=200)),
            ],
        ),
    ]
