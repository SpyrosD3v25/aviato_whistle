
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
