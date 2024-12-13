from django.shortcuts import render, redirect
from .models import RepairRequest
from .forms import RepairRequestForm

# Create your views here.
def post_request(request):
    if request.method == 'POST':
        form = RepairRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recent_requests')
    else:
        form = RepairRequestForm()
    return render(request, 'repairs/post_request.html', {'form': form})

def recent_requests(request):
    requests = RepairRequest.objects.all().order_by('-created_at')
    return render(request, 'repairs/recent_requests.html', {'requests': requests})
