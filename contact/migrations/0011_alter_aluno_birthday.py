# Generated by Django 5.1 on 2024-08-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_alter_aluno_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]