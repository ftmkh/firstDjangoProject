# Generated by Django 5.1.4 on 2025-01-26 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_alter_comments_email_alter_comments_name'),
        ('maktab7app', '0010_post_created_at_alter_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='maktab7app.post'),
        ),
    ]
