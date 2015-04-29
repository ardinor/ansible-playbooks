#!/bin/python

"""
Django Password Generator for Graphite
Takes one argument the unencrypted password then prints out the encrypted
one as generated by Django's make_password function.

The make_password function needs settings to be configured before it'll run
so we set the DJANGO_SETTINGS_MODULE environment variable to the Graphite
settings
"""

import os
import argparse

parser = argparse.ArgumentParser(description='Prints a Django hashed password')
parser.add_argument('password', type=str)
args = parser.parse_args()

os.environ['DJANGO_SETTINGS_MODULE'] = 'graphite.settings'

from django.contrib.auth.hashers import make_password

print make_password(args.password)
