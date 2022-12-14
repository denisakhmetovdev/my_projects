# Generated by Django 4.1.1 on 2022-09-30 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="changed",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Изменён"),
        ),
        migrations.AlterField(
            model_name="project",
            name="is_done",
            field=models.BooleanField(default=False, verbose_name="Выполнено"),
        ),
    ]
