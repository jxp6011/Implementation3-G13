# Generated by Django 3.2.25 on 2024-10-24 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yours', '0010_post_and_comment_ordering'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='content_type_fk',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='object_pk',
            new_name='object_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='yours.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
