from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from link.forms import LinkForm
from link.models import Link

# Create your views here.


def home(request):
    no_of_discounted = 0
    error = None

    form = LinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Oops..! Not able to get product title or price from the link provided."
        except Exception:
            error = "Oops..! Something went wrong."

    form = LinkForm()

    qs = Link.objects.all()
    no_of_items = qs.count()

    if no_of_items > 0:
        discount_list = [
            item for item in qs if item.old_price > item.current_price]
        no_of_discounted = len(discount_list)

    context = {
        'no_of_discounted': no_of_discounted,
        'items': qs,
        'error': error,
        'no_of_items': no_of_items,
        'form': form,
    }

    return render(request, 'link/main.html', context=context)


def update_items(request):
    qs = Link.objects.all()
    for item in qs:
        item.save()
    return redirect('home')


class DeleteProductView(DeleteView):
    model = Link
    template_name = "link/confirm_delete.html"
    success_url = reverse_lazy('home')
