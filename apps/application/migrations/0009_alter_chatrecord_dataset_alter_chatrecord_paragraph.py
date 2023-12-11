# Generated by Django 4.1.10 on 2023-12-11 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0001_initial'),
        ('application', '0008_remove_application_api_key_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatrecord',
            name='dataset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataset.dataset', verbose_name='数据集'),
        ),
        migrations.AlterField(
            model_name='chatrecord',
            name='paragraph',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataset.paragraph', verbose_name='段落id'),
        ),
    ]
