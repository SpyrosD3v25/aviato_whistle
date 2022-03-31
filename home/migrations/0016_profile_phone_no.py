
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210705_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
