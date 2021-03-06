from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):

    def handle(self, *args, **options):
        for fixture in ('initial_approaches', 'initial_countries',
                        'initial_geo_scope', 'initial_phases',
                        'initial_themes', 'initial_types_of_outcome',
                        'initial_languages'):
            call_command('loaddata', fixture)
