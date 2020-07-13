# Generated by Django 2.2.12 on 2020-06-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(blank=True, max_length=255)),
                ('module_code', models.CharField(blank=True, max_length=255)),
                ('no_of_patients', models.IntegerField(default=0)),
                ('web_space', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('cgst', models.IntegerField(default=0)),
                ('sgst', models.IntegerField(default=0)),
                ('gst', models.IntegerField(default=0)),
                ('total_amount', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]