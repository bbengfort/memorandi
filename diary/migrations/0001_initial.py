# Generated by Django 3.1.3 on 2020-12-03 02:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Name of the country or region', max_length=255)),
                ('iso_code', models.CharField(help_text='ISO code for the region or country', max_length=3)),
                ('region_type', models.PositiveSmallIntegerField(choices=[(0, 'continent'), (1, 'country'), (2, 'region')], default=1, help_text='Type of geographic region')),
                ('parent', models.ForeignKey(blank=True, default=None, help_text='The geographic entity that contains the current entity', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='diary.geoentity')),
            ],
            options={
                'verbose_name': 'geographic entity',
                'verbose_name_plural': 'geographic entities',
                'db_table': 'geo_entities',
                'unique_together': {('name', 'iso_code', 'region_type')},
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(blank=True, default=None, help_text='A place name e.g. Home or Work', max_length=255, null=True)),
                ('latitude', models.FloatField(blank=True, default=None, help_text='Decimal latitude of the location', null=True)),
                ('longitude', models.FloatField(blank=True, default=None, help_text='Decimal longitude of the location', null=True)),
                ('ipaddr', models.GenericIPAddressField(blank=True, default=None, help_text='The originating IP address of the location', null=True)),
                ('address', models.CharField(blank=True, default=None, help_text='A specific address on a single line', max_length=255, null=True)),
                ('city', models.CharField(blank=True, default=None, help_text='Name of the city specified by the address', max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, default=None, help_text='Postal code of the address or other coded identification', max_length=31, null=True)),
                ('quick_select', models.BooleanField(default=False, help_text='Allow this location to appear in quick select forms')),
                ('country', models.ForeignKey(blank=True, default=None, help_text='Entity representing the Country of the address', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='diary.geoentity')),
                ('region', models.ForeignKey(blank=True, default=None, help_text='Entity representing the Region, Province, or State of the address', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='diary.geoentity')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
                'db_table': 'locations',
                'ordering': ('-modified',),
                'get_latest_by': 'modified',
                'unique_together': {('name', 'address', 'city', 'country', 'region', 'postal_code'), ('name', 'latitude', 'longitude')},
            },
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', models.DateField(default=datetime.date.today, help_text='Date of the diary entry', unique=True)),
                ('memo', models.CharField(blank=True, default=None, help_text='A brief description of the day, e.g. the highlights', max_length=255, null=True)),
                ('entry', models.TextField(blank=True, default=None, help_text='The diary entry for the day (in Markdown)', null=True)),
                ('private', models.BooleanField(default=False, help_text='If the entry contains sensitive or private information')),
                ('feeling', models.SmallIntegerField(blank=True, choices=[(-2, 'terrible'), (-1, 'poor'), (0, 'fair'), (1, 'good'), (2, 'excellent')], default=0, help_text='A Likert scale of your general feeling about the day')),
                ('author', models.ForeignKey(help_text='The author of the diary entry', on_delete=django.db.models.deletion.PROTECT, related_name='memos', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(blank=True, help_text='The location where the diary entry was written', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='memos', to='diary.location')),
            ],
            options={
                'verbose_name': 'Memorandum',
                'verbose_name_plural': 'Memoranda',
                'db_table': 'memos',
                'ordering': ('-date',),
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='Tabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('desktop_windows', models.PositiveSmallIntegerField(blank=True, default=None, help_text='The number of desktop windows open', null=True)),
                ('desktop_tabs', models.PositiveSmallIntegerField(blank=True, default=None, help_text='The total number of desktop tabs open in all windows', null=True)),
                ('mobile_tabs', models.PositiveSmallIntegerField(blank=True, default=None, help_text='The number of tabs open on your mobile device', null=True)),
                ('tablet_tabs', models.PositiveSmallIntegerField(blank=True, default=None, help_text='The number of tabs open on your tablet device', null=True)),
                ('memo', models.OneToOneField(help_text='The memo associated with the tabs count', on_delete=django.db.models.deletion.CASCADE, related_name='tabs', to='diary.memo')),
            ],
            options={
                'verbose_name': 'Browser Tab Count',
                'verbose_name_plural': 'Browser Tab Counts',
                'db_table': 'browser_tabs',
                'ordering': ('-memo__date',),
                'get_latest_by': 'memo__date',
            },
        ),
    ]
