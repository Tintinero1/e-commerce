# Generated by Django 2.1.5 on 2019-04-07 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Nombre')),
                ('content', models.CharField(max_length=1024)),
                ('precio', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='gallery')),
                ('carritochecker', models.BooleanField(default=False)),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.seccion')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
