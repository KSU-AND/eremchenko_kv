from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from ...models.language import Language
from ...models.area import Area
from ...models.genus import Genus
from ...models.family import Family


def fill_families():
    with open("fut_in_pst_typology/management/csvs/families.csv", "r", encoding="utf-8") as f:
        for line in f:
            try:
                Family.objects.create(name=line.strip())
            except IntegrityError:
                pass

def fill_areas():
    with open("fut_in_pst_typology/management/csvs/areas.csv", "r", encoding="utf-8") as f:
        for line in f:
            code, name = line.strip().split(",")
            try:
                Area.objects.create(code=code, name=name,)
            except IntegrityError:
                pass

def fill_genuses():
    with open("fut_in_pst_typology/management/csvs/genuses.csv", "r", encoding="utf-8") as f:
        for line in f:
            try:
                Genus.objects.create(name=line.strip())
            except IntegrityError:
                pass

def fill_languages():
    with open("fut_in_pst_typology/management/csvs/languages.csv", "r", encoding="utf-8") as f:
        for line in f:
            code, name, genus, family = line.strip().split(",")
            try:
                Language.objects.create(code=code,
                                      name=name, 
                                      genus=Genus.objects.get(name=genus),
                                      family=Family.objects.get(name=family))
            except IntegrityError:
                pass


class Command(BaseCommand):
    help = 'Initial database filling'

    def add_arguments(self, parser):
        parser.add_argument('--area', action='store_true')
        parser.add_argument('--genus', action='store_true')
        parser.add_argument('--family', action='store_true')
        parser.add_argument('--language', action='store_true')
    
    def handle(self, *args, **options):
        if options["area"]: fill_areas()
        if options["genus"]: fill_genuses()
        if options["family"]: fill_families()
        if options["language"]: fill_languages()