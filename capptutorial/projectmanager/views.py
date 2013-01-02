from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from projectmanager.models import Project
from projectmanager.serializers import ProjectSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
            'projects': reverse('project-list', request=request, format=format)
        })


@ensure_csrf_cookie
def home(request):
    return render(request, 'index.html', {})


class ProjectList(generics.ListCreateAPIView):
    model = Project
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Project
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProjectSerializer
