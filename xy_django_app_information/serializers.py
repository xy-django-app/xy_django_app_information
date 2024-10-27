# -*- coding: UTF-8 -*-


from .models import *
from rest_framework import viewsets
from xy_admin_model_serializer.Admin_ModelSerializer import *


class SRegion(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MRegion
        fields = "__all__"


class VSRegion(viewsets.ModelViewSet):
    queryset = MRegion.objects.all()
    serializer_class = SRegion


class SVersion(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MVersion
        fields = "__all__"


class VSVersion(viewsets.ModelViewSet):
    queryset = MVersion.objects.all()
    serializer_class = SVersion


class SDevelopment(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MVersion
        fields = "__all__"


class VSDevelopment(viewsets.ModelViewSet):
    queryset = MVersion.objects.all()
    serializer_class = SDevelopment


class SSystem(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MSystem
        fields = "__all__"


class VSSystem(viewsets.ModelViewSet):
    queryset = MSystem.objects.all()
    serializer_class = SSystem


class SDevice(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MDevice
        fields = "__all__"


class VSDevice(viewsets.ModelViewSet):
    queryset = MDevice.objects.all()
    serializer_class = SDevice
