# Generated by Django 2.2 on 2019-04-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('file', models.FileField(upload_to='static/img/gallery')),
            ],
        ),
        migrations.AlterField(
            model_name='test',
            name='file',
            field=models.FileField(upload_to='static/img/gallery'),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
