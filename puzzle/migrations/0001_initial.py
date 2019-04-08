# Generated by Django 2.1.7 on 2019-04-08 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.IntegerField(db_index=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('suburb', models.CharField(max_length=20, null=True)),
                ('postcode', models.IntegerField()),
                ('street', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='level',
            fields=[
                ('level_id', models.IntegerField(primary_key=True, serialize=False)),
                ('level_desc', models.CharField(max_length=10)),
                ('level_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('photo_desc', models.CharField(max_length=300, null=True)),
                ('image', models.ImageField(blank=True, upload_to='puzzle/')),
                
            ],
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('puzzle_id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('startTime', models.DateTimeField(verbose_name='time start play')),
                ('endTime', models.DateTimeField(verbose_name='time finish play')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puzzle.level')),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puzzle.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('specie_id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('specie_name', models.CharField(blank=True, max_length=300, null=True)),
                ('specie_desc', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('user_score', models.IntegerField(default=0)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puzzle.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Zoo',
            fields=[
                ('zoo_id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('zoo_logo', models.ImageField(blank=True, null=True, upload_to='puzzle')),
                ('zoo_name', models.CharField(max_length=200, null=True)),
                ('zoo_city', models.CharField(max_length=20, null=True)),
                ('zoo_suburb', models.CharField(max_length=20, null=True)),
                ('zoo_post', models.IntegerField()),
                ('zoo_street', models.CharField(max_length=50, null=True)),
                ('zoo_open', models.DateTimeField(verbose_name='zoo open time')),
                ('zoo_close', models.DateTimeField(verbose_name='zoo close time')),
            ],
        ),
        migrations.AddField(
            model_name='puzzle',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puzzle.Specie'),
        ),
        migrations.AddField(
            model_name='photo',
            name='specie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='puzzle.Specie'),
        ),
    ]
