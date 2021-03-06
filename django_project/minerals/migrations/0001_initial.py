# Generated by Django 2.1.3 on 2018-12-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image_filename', models.CharField(max_length=500)),
                ('image_caption', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=500)),
                ('formula', models.CharField(max_length=500)),
                ('strunz_classification', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=500)),
                ('crystal_system', models.CharField(max_length=500)),
                ('unit_cell', models.CharField(max_length=500)),
                ('crystal_symmetry', models.CharField(max_length=500)),
                ('cleavage', models.CharField(max_length=500)),
                ('mohs_scale_hardness', models.CharField(max_length=500)),
                ('luster', models.CharField(max_length=500)),
                ('streak', models.CharField(max_length=500)),
                ('diaphaneity', models.CharField(max_length=255)),
                ('optical_properties', models.CharField(max_length=500)),
                ('refractive_index', models.CharField(max_length=500)),
                ('crystal_habit', models.CharField(max_length=500)),
                ('specific_gravity', models.CharField(max_length=500)),
                ('group', models.CharField(max_length=500)),
            ],
        ),
    ]
