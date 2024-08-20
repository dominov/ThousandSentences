from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from sentence.forms import SentenceForm
from sentence.models import Sentence


# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class SentenceListView(ListView):
    model = Sentence
    paginate_by = 10



@method_decorator(staff_member_required, name='dispatch')
class SentenceDetailView(DetailView):
    model = Sentence


@method_decorator(staff_member_required, name='dispatch')
class SentenceCreateView(CreateView):
    model = Sentence
    form_class = SentenceForm
    # fields = ['topic', 'phrase_english', 'phrase_spanish', 'keywords', 'difficulty']
    success_url = reverse_lazy('sentences:sentences')


@method_decorator(staff_member_required, name='dispatch')
class SentenceUpdateView(UpdateView):
    model = Sentence
    fields = ['topic', 'phrase_english', 'phrase_spanish', 'keywords', 'difficulty']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('sentences:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class SentenceDeleteView(DeleteView):
    model = Sentence
    success_url = reverse_lazy('sentences:sentences')
