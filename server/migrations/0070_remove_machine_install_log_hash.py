# Generated by Django 1.11 on 2018-04-25 18:29


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0069_remove_machine_install_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='install_log_hash',
        ),
    ]
