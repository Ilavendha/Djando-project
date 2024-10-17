from django.shortcuts import render
from .models import Study

def study_list(request):
    studies = Study.objects.all()  # Fetch all studies
    return render(request, 'myapp/study_list.html', {'studies': studies})
