# Generated by Django 4.1.3 on 2023-03-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210528_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.DecimalField(decimal_places=8, max_digits=8)),
                ('position', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
