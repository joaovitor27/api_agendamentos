from rest_framework import serializers
from .models import Reservation, Workstations


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'work_stations', 'employee_name', 'shift', 'appointment_date', 'created']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Reservation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.work_stations = validated_data.get('work_stations', instance.work_stations)
        instance.employee_name = validated_data.get('employee_name', instance.employee_name)
        instance.shift = validated_data.get('shift', instance.shift)
        instance.appointment_date = validated_data.get('appointment_date', instance.appointment_date)
        instance.save()
        return instance


class WorkstationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workstations
        fields = ['id', 'work_stations']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Workstations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.work_stations = validated_data.get('work_stations', instance.work_stations)
        instance.save()

        return instance

    def delete(self, instance, validated_data):
        ...
