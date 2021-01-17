# Generated by Django 3.1.1 on 2020-09-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200923_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]
