from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),  # Replace '0001_initial' with your latest migration
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]