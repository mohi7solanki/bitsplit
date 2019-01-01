# Generated by Django 2.1.4 on 2019-01-01 20:34

import bitsplit.corpus.models.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0002_auto_20181231_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accent_color', models.CharField(blank=True, default='#707070', max_length=7)),
                ('bitset_type', models.CharField(choices=[('public', 'Public'), ('restricted', 'Restricted'), ('private', 'Private')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('applies_to', models.IntegerField(choices=[(1, 'Posts and comments'), (2, 'Posts'), (3, 'Comments only')])),
                ('voilation_reason', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bitset',
            name='approved_submitters',
            field=models.ManyToManyField(blank=True, related_name='bitsets_approved_submitted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bitset',
            name='banned_users',
            field=models.ManyToManyField(blank=True, related_name='bitsets_banned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bitset',
            name='muted_users',
            field=models.ManyToManyField(blank=True, related_name='bitsets_muted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bitset',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bit',
            name='bit_type',
            field=models.CharField(choices=[('url', 'URL'), ('txt', 'Text'), ('img', 'Image')], max_length=3),
        ),
        migrations.AlterField(
            model_name='bit',
            name='users_bookmarked',
            field=models.ManyToManyField(blank=True, related_name='bookmarked_bits', to=settings.AUTH_USER_MODEL),
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
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corpus.BitSet'),
        ),
        migrations.AddField(
            model_name='bitset',
            name='option',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='corpus.Option'),
        ),
    ]
