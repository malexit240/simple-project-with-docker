from django.views.generic import FormView
from .forms import ItemForm
from .models import Item
from django.shortcuts import reverse

class ItemView(FormView):
    template_name = 'dj_app/item.html'
    form_class = ItemForm
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context

    def form_valid(self, form):
        self.success_url = self.success_url or reverse('items')

        Item.objects.create(name=form.data['name'])

        return super().form_valid(form)