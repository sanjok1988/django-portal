from rest_framework import serializers

from team.models import Team


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'member_name', 'position', 'details', 'photo', 'social_links', 'status']
