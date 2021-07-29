from django.shortcuts import render
from projects.models import Project #Import the class with the database's info


# Create your views here.
#Every view function needs to have a context dictionary to assign the Queryset (collection)

def project_index(request):
    projects = Project.objects.all()  #select all the elements in the Project table
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

