# Generated by Django 2.1.4 on 2019-01-01 20:18

import bitsplit.corpus.models.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0002_auto_20190101_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('upvotes', models.PositiveIntegerField(default=0)),
                ('downvotes', models.PositiveIntegerField(default=0)),
                ('author_username', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
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
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='bit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='corpus.Bit'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='corpus.Comment'),
        ),
    ]
