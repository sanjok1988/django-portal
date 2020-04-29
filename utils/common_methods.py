from rest_framework import mixins, viewsets
from rest_framework.response import Response

# enable disable status 1 and 0
from utils.mixins import UpdateModelMixin


# generic method to
# change the status from 1 to 0
# using customized UpdateModelMixin
class EnableDisableViewSet(
    UpdateModelMixin,
    viewsets.GenericViewSet
):
    print("here")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        print(instance)
        if instance.status == 1:
            instance.status = 0
        else:
            instance.status = 1

        instance.save(update_fields=["status"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
