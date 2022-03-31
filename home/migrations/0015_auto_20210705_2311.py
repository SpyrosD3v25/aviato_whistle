
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210705_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='dateTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
