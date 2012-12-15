from projectmanager.models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    partial = True

    class Meta:
        model = Project
        read_only_fields = ('created', 'modified')
        fields = ("url", "project_name", "short_description", "start_date", "end_date", "created", "modified")
