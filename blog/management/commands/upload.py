""" upload markdown file to server or database.
"""
import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', help='markdown file', required=True)

    def handle(self, *args, **options):
        file = options.get('file')

        print(file)

