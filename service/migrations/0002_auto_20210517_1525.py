# Generated by Django 3.2 on 2021-05-17 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='galery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleryblog', to='service.galery', verbose_name='gallery_blog'),
        ),
        migrations.AlterField(
            model_name='galery',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorygalery', to='service.category', verbose_name='category_galery'),
        ),
    ]
