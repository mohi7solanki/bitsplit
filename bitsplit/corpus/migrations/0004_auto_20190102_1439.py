# Generated by Django 2.1.4 on 2019-01-02 14:39

import bitsplit.corpus.models.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0003_auto_20190101_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('accent_color', models.CharField(blank=True, default='#707070', max_length=7)),
                ('bitset_type', models.CharField(choices=[('public', 'Public'), ('restricted', 'Restricted'), ('private', 'Private')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('applies_to', models.IntegerField(choices=[(1, 'Posts and comments'), (2, 'Posts'), (3, 'Comments only')])),
                ('violation_reason', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='bitset',
            options={'verbose_name_plural': 'BitSets'},
        ),
        migrations.AddField(
            model_name='bitset',
            name='approved_submitters',
            field=models.ManyToManyField(blank=True, related_name='bitsets_approved_in', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bitset',
            name='banned_users',
            field=models.ManyToManyField(blank=True, related_name='bitsets_banned_in', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bitset',
            name='muted_users',
            field=models.ManyToManyField(blank=True, related_name='bitsets_muted_in', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bitset',
            name='logo',
            field=models.ImageField(upload_to=bitsplit.corpus.models.utils.UploadPath._get_file_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(upload_to=bitsplit.corpus.models.utils.UploadPath._get_file_path),
        ),
        migrations.AddField(
            model_name='rule',
            name='bitset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='corpus.BitSet'),
        ),
        migrations.AddField(
            model_name='option',
            name='bit',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='corpus.BitSet'),
        ),
    ]