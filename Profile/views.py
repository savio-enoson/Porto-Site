from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import render_to_string

from django.utils.formats import date_format, number_format
from django.utils.timezone import localdate
import datetime
import json

from Profile.models import Project

project_templates = {
    'parkibara': "Projects/parkibara.html",
    'genetic_ka': "Projects/genetic_ka.html",
    'sp_shooter': "Projects/sp_shooter.html",
    'warehouse_sim': "Projects/warehouse_sim.html",
    'erp_toko': "Projects/erp_toko.html",
}


def get_profile(request):
    as_json = request.GET.get('as_json')
    context = {
        'app': {'name': 'profile', 'page': 'null'},
        'template': "General/base.html" if as_json else "General/layout.html",
        "projects": Project.objects.filter(featured=True),
        'as_json': as_json
    }
    if as_json:
        page_content = render_to_string('Profile/index.html', context)

        return JsonResponse({
            'content': page_content,
            'title': "Savio's Portfolio Site"
        })
    else:
        return render(request, 'Profile/index.html', context)


def get_project(request, project_name=None):
    as_json = request.GET.get('as_json')
    if not project_name:
        project_name = request.GET.get('name')

    index = project_name not in project_templates

    project_list = Project.objects.all()
    years = list(Project.objects.values_list('date__year', flat=True).distinct())

    types = list(project_list.filter(type__isnull=False).values_list('type', flat=True).distinct())
    types = [word.strip() for string in types for word in string.split(',')]

    topics = list(project_list.values_list('topics', flat=True).distinct())
    topics = [word.strip() for string in topics for word in string.split(',')]

    instances = list(project_list.values_list('instance', flat=True).distinct())

    context = {
        'app': {'name': 'projects', 'page': 'null' if index else project_name.replace("_", " ").title()},
        'template': "General/base.html" if as_json else "General/layout.html",
        'content': None if index else render_to_string(project_templates[project_name],
           {'project': Project.objects.get(template_name=project_name)}),
        'project': project_list if index else Project.objects.get(template_name=project_name),
        'years': years, 'types': types, 'topics': topics, 'instances': instances,
        'as_json': as_json
    }

    if as_json:
        page_content = render_to_string(
            'Projects/index.html' if index
            else project_templates[project_name], context)

        return JsonResponse({
            'content': page_content,
            'title': f"Projects | {'All' if index else project_name.replace('_', ' ').title()}"
        })
    else:
        return render(request, 'Projects/index.html', context)
