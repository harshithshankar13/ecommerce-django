# Generated by Django 2.2.4 on 2019-12-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('NO', 'SELECT CATEGORY'), ('MP', 'Mens Products'), ('WP', 'Womens Products'), ('KD', 'Kids Products'), ('SP', 'Stationery Products'), ('HKP', 'Home Kitchen Products'), ('SFP', 'Sports Fitness Products'), ('EP', 'Electronics Products')], default='SELECT CATEGORY', max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('NO', 'SELECT CATEGORY'), ('MP', 'Mens Products'), ('WP', 'Womens Products'), ('KD', 'Kids Products'), ('SP', 'Stationery Products'), ('HKP', 'Home Kitchen Products'), ('SFP', 'Sports Fitness Products'), ('EP', 'Electronics Products')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('P', 'primary'), ('D', 'danger')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
