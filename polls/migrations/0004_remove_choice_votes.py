# Generated by Django 4.1 on 2022-09-20 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_alter_question_end_date_vote"),
    ]

    operations = [
        migrations.RemoveField(model_name="choice", name="votes",),
    ]