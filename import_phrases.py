import pandas as pd
from django.core.management.base import BaseCommand
from sentence.models import Level, Topic, Sentence


class Command(BaseCommand):
    help = 'Import phrases from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        data = pd.read_excel(file_path)

        for _, row in data.iterrows():
            level, created = Level.objects.get_or_create(name=row['level'])
            theme, created = Topic.objects.get_or_create(level=level,
                                                         min_completed_sentences=row.get('min_completed_sentences', 6))
            Sentence.objects.create(
                theme=theme,
                phrase_spanish=row['phrase_spanish'],
                phrase_english=row['phrase_english'],
                keywords=row['keywords'],
                difficulty=row.get('difficulty')
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported phrases'))
