# Generated by Django 5.0.1 on 2024-01-17 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='complain',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('complain_name', models.CharField(max_length=20)),
                ('complain_message', models.TextField(max_length=25)),
                ('complain_datetime', models.DateTimeField(max_length=10)),
                ('complain_status', models.IntegerField(choices=[('0', 'Inactive'), ('1', 'Active')])),
            ],
        ),
        migrations.CreateModel(
            name='ContactTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('feedback_desk', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=255)),
                ('policy_details', models.TextField()),
                ('policy_type', models.CharField(max_length=50)),
                ('policy_photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('policy_agency', models.CharField(max_length=100)),
                ('policy_target_audience', models.CharField(max_length=100)),
                ('policy_eligible_castes', models.CharField(max_length=100)),
                ('policy_applicable_state', models.CharField(max_length=50)),
                ('policy_residence_area', models.CharField(max_length=50)),
                ('policy_disability_status', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('policy_minority_status', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('policy_bpl_status', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('policy_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=15)),
                ('occupation', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('role', models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], default='user', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_method', models.BigIntegerField(choices=[('0', 'online'), ('1', 'offline')])),
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('payment_status', models.IntegerField(choices=[('0', 'Inactive'), ('1', 'Active')])),
                ('application_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.policy')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('policy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.policy')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comments', models.TextField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='aadhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_number', models.BigIntegerField()),
                ('aadhar_middlename', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=20)),
                ('phonenumber', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('cast', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('document', models.CharField(max_length=50)),
                ('residencearea', models.CharField(max_length=50)),
                ('disability_status', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('minority_status', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('bpl_status', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('aadhar_firstname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
