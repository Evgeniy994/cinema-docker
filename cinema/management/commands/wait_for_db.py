import time
from django.db import connections as connect
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Wait for DB"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database startup ...")
        db_connection = connect["default"]
        while not db_connection:
            try:
                db_connection = connect["default"]
            except OperationalError:
                self.stdout.write("Already waiting ...")
                time.sleep(1)

        self.stdout.write("Database connection successful!")
