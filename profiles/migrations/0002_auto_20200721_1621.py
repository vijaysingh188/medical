# Generated by Django 3.0 on 2020-07-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indivdualuserprofile',
            name='first_name',
            field=models.CharField(default='john', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indivdualuserprofile',
            name='last_name',
            field=models.CharField(default='smith', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indivdualuserprofile',
            name='middle_name',
            field=models.CharField(default='s', max_length=150),
            preserve_default=False,
        ),
    ]