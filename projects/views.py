from django.shortcuts import render
from projects.models import Project, Category

# Create your views here.

#Project Index - Shows A Snippet of Information About Each Project
def project_index(request): 
    projects = Project.objects.latest('id')
    context = {
        'projects' : projects
    }
    return render(request, 'project_index.html', context)

#Project Category - Shows A Snippet of Information About Each Project For A Particular Category
def project_category(request, category):
    projects = Project.objects.filter(
        categories__name__contains = category
    )
    context = {
        "category": category, 
        "projects": projects
    }
    return render(request, 'project_category.html', context)

#Project Detail - Shows More Information on A Particular Topic
def project_detail(request, pk): 
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)