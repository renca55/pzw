from django.db import migrations
from django.utils.timezone import make_aware
from datetime import datetime

def add_test_data(apps, schema_editor):
    LanguageExchange = apps.get_model('pzwebapp', 'LanguageExchange')
    User = apps.get_model('auth', 'User')

    # Kreiranje korisnika
    user1 = User.objects.create(username='user1', email='user1@example.com')
    user2 = User.objects.create(username='user2', email='user2@example.com')

    # Dodavanje testnih razmjena jezika
    exchange1 = LanguageExchange.objects.create(
        name='Engleski u Španjolski',
        description='Razmjena jezika između engleskog i španjolskog.',
        language_offered='English',
        language_requested='Spanish',
        date=make_aware(datetime(2024, 12, 20, 18, 0))
    )
    exchange1.participants.add(user1, user2)

    exchange2 = LanguageExchange.objects.create(
        name='Njemački u Francuski',
        description='Razmjena jezika između njemačkog i francuskog.',
        language_offered='German',
        language_requested='French',
        date=make_aware(datetime(2024, 12, 21, 16, 0))
    )
    exchange2.participants.add(user1)

class Migration(migrations.Migration):

    dependencies = [
        ('pzwebapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_test_data),
    ]
