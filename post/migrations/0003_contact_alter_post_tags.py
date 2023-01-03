# Generated by Django 4.1.3 on 2023-01-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('message_date', models.DateTimeField()),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'contacts',
                'verbose_name_plural': 'contact',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='post.tag'),
        ),
    ]
