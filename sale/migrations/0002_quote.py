# Generated by Django 2.1.3 on 2018-11-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('email_address', models.EmailField(max_length=100)),
                ('preferred_contact_method', models.CharField(choices=[('phone', 'Phone Number'), ('email', 'Email Address'), ('both', 'Both')], max_length=50)),
                ('quantity', models.IntegerField()),
                ('condition', models.CharField(choices=[('FN', 'Factory New'), ('NE', 'New Material'), ('NS', 'New Surplus'), ('OH', 'Overhauled'), ('SV', 'Servicable'), ('RP', 'Repariable'), ('AR', 'As Removed')], max_length=50)),
                ('priority', models.CharField(choices=[('AOG', 'Aircraft On Ground'), ('Immediate', 'Within 1-2 Weeks'), ('Flexible', 'No Specific Time')], max_length=50)),
                ('accepted_terms', models.BooleanField()),
            ],
            options={
                'db_table': 'quote',
            },
        ),
    ]
