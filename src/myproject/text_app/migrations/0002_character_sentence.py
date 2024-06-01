# Generated by Django 4.2.13 on 2024-05-29 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('text_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名前')),
                ('icon', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='アイコン')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': 'キャラクター',
                'db_table': 'character',
            },
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='文章')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text_app.novel', verbose_name='小説')),
                ('speaker', models.ManyToManyField(to='text_app.character', verbose_name='発言者')),
            ],
            options={
                'verbose_name_plural': '文章',
                'db_table': 'sentence',
            },
        ),
    ]
