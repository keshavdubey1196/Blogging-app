# Generated by Django 4.1.7 on 2023-03-09 20:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_blog_content"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="subtitle",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="tags",
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
    ]
