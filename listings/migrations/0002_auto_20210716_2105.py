# Generated by Django 3.2.5 on 2021-07-16 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='photo_1',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_10',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_11',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_12',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_13',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_14',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_15',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_16',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_17',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_18',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_19',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_2',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_20',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_3',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_4',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_5',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_6',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_7',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_8',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_9',
        ),
        migrations.CreateModel(
            name='ListingPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='listing_photos/%Y/%m/%d/')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='listing_photos', to='listings.listing')),
            ],
        ),
    ]
