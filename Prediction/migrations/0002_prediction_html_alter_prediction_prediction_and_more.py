# Generated by Django 4.0.8 on 2023-03-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prediction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='html',
            field=models.FileField(blank=True, null=True, upload_to='html_files'),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='prediction',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='text',
            field=models.TextField(),
        ),
    ]