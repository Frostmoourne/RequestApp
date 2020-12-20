from rest_framework import serializers

from .models import Client, Request, Employee


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'phone')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'position')


class RequestUpdateSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    responsible = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())

    class Meta:
        model = Request
        fields = ('id', 'text', 'responsible', 'client')


class RequestReadSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    responsible = EmployeeSerializer()

    class Meta:
        model = Request
        fields = ('id', 'text', 'responsible', 'client')

