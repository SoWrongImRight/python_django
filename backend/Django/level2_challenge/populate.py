import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','level2_challenge.settings')

import django
django.setup()

from random import randint
from faker import Faker

from app_one.models import User

fake = Faker()

def populate(n=10):
    for entry in range(n):
        fake_fname = fake.name()
        fake_lname = fake.name()
        fake_mail = fake.email()

        usergen = User.objects.get_or_create(fname=fake_fname,lname=fake_lname,mail=fake_mail)[0]

if __name__ == '__main__':
    print("Populating Users")
    populate()
    print("Populating Complete!")
