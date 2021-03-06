# Generated by Django 4.0.5 on 2022-06-25 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Image')),
                ('headline', models.CharField(max_length=100, verbose_name='Headline')),
                ('description', models.TextField(max_length=100, null=True, verbose_name='Description')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Price')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_edited', models.DateTimeField(auto_now_add=True, verbose_name='Date edited')),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='Date published')),
                ('status', models.CharField(choices=[('to_moderate', 'To Moderate'), ('published', 'Published'), ('canceled', 'Canceled')], default=('to_moderate', 'To Moderate'), max_length=100, verbose_name='Status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='accounts.profile', verbose_name='Advertisement')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='webapp.category', verbose_name='Advertisement')),
            ],
            options={
                'verbose_name': 'Advertisement',
                'verbose_name_plural': 'Advertisements',
                'db_table': 'advertisement',
            },
        ),
    ]
