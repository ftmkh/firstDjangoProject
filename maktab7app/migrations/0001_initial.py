# Generated by Django 4.2 on 2024-12-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='images/default.png', upload_to='')),
                ('author', models.CharField(max_length=250)),
                ('published_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
