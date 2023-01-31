from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from core import tasks
from core.models import Job


def index(request):
    query = Job.objects.order_by('-ran_on')

    paginator = Paginator(query, per_page=15)

    page = request.GET.get('page', 1)

    return render(request, 'core/index.html', {'records': paginator.get_page(page)})


def run(request):
    if request.method == 'POST':
        tasks.manual.delay()

        return redirect('core:index')

    return render(request, 'core/run.html')
