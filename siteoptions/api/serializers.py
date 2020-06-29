from rest_framework import serializers

from siteoptions.models import SiteOptions


class ListOptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteOptions
        fields = ['name', 'value']
