# Generated by Django 3.1 on 2022-06-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0002_auto_20220602_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyinformation',
            options={'ordering': ['my_order'], 'verbose_name': 'Կոնտակտային տվյալ', 'verbose_name_plural': 'Կոնտակտային տվյալներ'},
        ),
        migrations.AlterModelOptions(
            name='footercategory',
            options={'ordering': ['my_order'], 'verbose_name': 'Footer -ի բաժին', 'verbose_name_plural': 'Footer -ի բաժիններ'},
        ),
        migrations.AlterModelOptions(
            name='footeritems',
            options={'ordering': ['my_order'], 'verbose_name': 'Footer -ի հղումներ', 'verbose_name_plural': 'Footer -ի հղումներ'},
        ),
        migrations.AlterModelOptions(
            name='socialsharebuttons',
            options={'ordering': ['my_order'], 'verbose_name': 'Սոց. ցանցի լոգո', 'verbose_name_plural': 'Սոց. ցանցերի լոգոներ'},
        ),
        migrations.AddField(
            model_name='companyinformation',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Դասավորել'),
        ),
        migrations.AddField(
            model_name='footercategory',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Դասավորել'),
        ),
        migrations.AddField(
            model_name='footeritems',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Դասավորել'),
        ),
        migrations.AddField(
            model_name='socialsharebuttons',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Դասավորել'),
        ),
    ]