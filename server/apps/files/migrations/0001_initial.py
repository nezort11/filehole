# Generated by Django 4.0.2 on 2022-02-19 20:57

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=16, max_length=40, prefix='', primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=255, upload_to='files', verbose_name='file')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'ordering': ['id'],
            },
        ),
    ]
