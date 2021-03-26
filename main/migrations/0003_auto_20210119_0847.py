# Generated by Django 3.1.2 on 2021-01-19 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210118_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.userroom'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentator_comments', to='main.comentator'),
        ),
    ]
