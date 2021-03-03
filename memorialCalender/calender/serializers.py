from django.db.models import fields
from .models import Calender
from rest_framework import serializers

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = ('title', 'start_day', 'cycle_with', 'cycle_unit')

    def create(self, validated_data, user_id):
        calender = super().create(validated_data)
        calender.set_user_id = user_id
        calender.save()
        return calender

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.start_day = validated_data.get('start_day', instance.start_day)
        instance.cycle_with = validated_data.get('cycle_with', instance.cycle_with)
        instance.cycle_unit = validated_data.get('cycle_unit', instance.cycle_unit)
        instance.save()
        return instance