# Generated by Django 4.1.5 on 2023-01-09 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_post', models.CharField(choices=[('a', 'article'), ('n', 'news')], default='a', max_length=1)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('header', models.CharField(default='нет заголовка', max_length=255)),
                ('body', models.TextField(default='здесь ничего нет')),
                ('rating', models.FloatField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_paper.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_paper.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_paper.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='cat',
            field=models.ManyToManyField(through='news_paper.PostCategory', to='news_paper.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='здесь ничего нет')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_paper.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
