from django.shortcuts import render, get_object_or_404
from .models import Project
from .forms import ContactForm


def home(request):
    projects = Project.objects.all()  # Получаем все проекты из базы
    context = {
        'projects': projects,
        'name': 'Ваше_имя',
        'job': 'Ваша_профессия'
    }
    return render(request, 'portfolio/index.html', context)


def contacts(request):
    context = {
        'phone': 'номер_телефона',
        'telegram': 'аккаунт_в_тг'
    }
    return render(request, 'portfolio/contacts.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project_detail.html', context)


def contanct(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'portfolio/contact_success.html', {'form': form})
    else:
        form = ContactForm()
    
    return render(request, 'portfolio/contact.html', {'form': form})