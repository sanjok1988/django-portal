from django.db import router
from rest_framework import routers

from siteoptions.api.views import OptionsViewSet

router = routers.SimpleRouter()

router.register(r'options', viewset=OptionsViewSet)

urlpatterns = [

]
urlpatterns += router.urls
