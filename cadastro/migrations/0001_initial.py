# Generated by Django 3.2.8 on 2021-11-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=int, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(blank=True, max_length=50, null=True)),
                ('sexo', models.CharField(choices=[('M', 'm'), ('F', 'f')], max_length=1)),
                ('altura', models.IntegerField()),
                ('peso', models.DecimalField(decimal_places=1, max_digits=7)),
                ('nascimento', models.DateTimeField()),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
