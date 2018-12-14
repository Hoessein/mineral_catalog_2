# Generated by Django 2.1.3 on 2018-12-14 15:07

from django.db import migrations

import json


def json_to_db(apps, schema_editor):
    Mineral = apps.get_model('minerals', 'Mineral')
    with open('minerals.json', encoding='utf8') as file:
        data = json.load(file)
        for mineral in data:
            try:
                Mineral(
                    name=mineral['name'],
                    image_filename=mineral.get('image filename', ""),
                    image_caption=mineral.get('image caption', ""),
                    category=mineral.get('category', ""),
                    formula=mineral.get('formula', ""),
                    strunz_classification=mineral.get('strunz classification', ""),
                    crystal_system=mineral.get('crystal system', ""),
                    unit_cell=mineral.get('unit cell', ""),
                    color=mineral.get('color', ""),
                    crystal_symmetry=mineral.get('crystal symmetry', ""),
                    cleavage=mineral.get('cleavage', ""),
                    mohs_scale_hardness=mineral.get('mohs scale hardness', ""),
                    luster=mineral.get('luster', ""),
                    streak=mineral.get('streak', ""),
                    diaphaneity=mineral.get('diaphaneity', ""),
                    optical_properties=mineral.get('optical properties', ""),
                    refractive_index=mineral.get('refractive index', ""),
                    crystal_habit=mineral.get('crystal habit', ""),
                    specific_gravity=mineral.get('specific gravity', ""),
                    group=mineral.get('group')
                ).save()
            except KeyError:
                continue


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]


    operations = [
        migrations.RunPython(json_to_db)
    ]