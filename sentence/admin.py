from django.contrib import admin
from .models import Level, Topic, Sentence, StudentStatistics

admin.site.register(Level)
admin.site.register(Topic)
admin.site.register(Sentence)
admin.site.register(StudentStatistics)