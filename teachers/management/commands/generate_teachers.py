from django.core.management.base import BaseCommand, CommandError
from teachers.models import Teacher
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = "Create your own number of teachers"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int)

    def handle(self, *args, **options):
        for i in range(options["number"]):
            t = Teacher.objects.create(
                name=fake.first_name(),
                last_name=fake.last_name(),
                birth_data=fake.date(),
                subject=fake.job(),
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully created teacher "%s"' % t.id)
        )
