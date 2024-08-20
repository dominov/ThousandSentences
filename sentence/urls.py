from django.urls import path

from .views import SentenceListView, SentenceDetailView, SentenceCreateView, SentenceUpdateView, SentenceDeleteView

sentences_url_patterns = ([
                    path('', SentenceListView.as_view(), name='sentences'),
                    path('<int:pk>/', SentenceDetailView.as_view(), name='detail'),
                    path('create/', SentenceCreateView.as_view(), name='create'),
                    path('update/<int:pk>/', SentenceUpdateView.as_view(), name='update'),
                    path('delete/<int:pk>/', SentenceDeleteView.as_view(), name='delete'),
                ], 'sentences')
