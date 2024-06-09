# myapp/management/commands/import_data.py

from django.core.management.base import BaseCommand
from exam.models import Course, Department
import pandas as pd

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        # Your data importing logic here
        csv_file_path = '~/Downloads/course_202402212100.csv'
        df = pd.read_csv(csv_file_path)

        for index, row in df.iterrows():
            print(f"{row=}")
            course = Course(
                course_id=row['course_id'],
                course_title=row['course_title'],
                dept=Department.objects.get(dept_id=row['dept_id']),
                Syllabus_year=row['Syllabus_year'],
                course_code=row['course_code']
            )
            course.save()

        self.stdout.write(self.style.SUCCESS('Data import completed.'))

