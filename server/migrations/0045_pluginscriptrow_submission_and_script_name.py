# Generated by Django 1.10 on 2016-08-10 06:27

from server.models import *
from django.db import migrations, models


def update_plugins(apps, schema_editor):

    PluginScriptRow = apps.get_model("server", "PluginScriptRow")
    PluginScriptSubmission = apps.get_model("server", "PluginScriptSubmission")

    for submission in PluginScriptSubmission.objects.all():
        for row in PluginScriptRow.objects.filter(submission=submission):
            row.submission_and_script_name = submission.plugin + ': ' + row.pluginscript_name
            row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0044_manual_20160809_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='pluginscriptrow',
            name='submission_and_script_name',
            field=models.TextField(db_index=True, default=' '),
            preserve_default=False,
        ),
        migrations.RunPython(update_plugins),
    ]
