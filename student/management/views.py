# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm

def study_list(request):
    studies = Study.objects.all()
    return render(request, 'myapp/study_list.html', {'studies': studies})

def create_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm()
    return render(request, 'myapp/create_study.html', {'form': form})

def delete_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == 'POST':
        study.delete()
        return redirect('study_list')
    return render(request, 'myapp/delete_study.html', {'study': study})
