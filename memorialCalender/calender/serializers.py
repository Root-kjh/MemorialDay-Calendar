from django.db.models import fields
from .models import Calender
from rest_framework import serializers

class CycleWithField(serializers.Field):
    
    CYCLE_WITH_TO_INTERNAL_DICT={
        "day": 0,
        "week": 1,
        "month": 2,
        "year": 3
    }

    CYCLE_WITH_TO_EXTERNAL_LIST = ["day", "week", "month", "year"]

    def to_internal_value(self, value):
        value = self.CYCLE_WITH_TO_INTERNAL_DICT[value]
        if type(value) is str:
            raise serializers.ValidationError("cycle_with is in (day, week, month, year)")
        return value

    def to_representation(self, data):
        return self.CYCLE_WITH_TO_EXTERNAL_LIST[data]

class CalenderSerializer(serializers.ModelSerializer):
    cycle_with = CycleWithField()
    class Meta:
        model = Calender
        fields = ('id', 'title', 'start_day', 'cycle_with', 'cycle_unit')

    def create(self, validated_data, user_id):
        calneder_data = {
            "user_id": user_id,
            "title": validated_data.pop("title"),
            "start_day": validated_data.pop("start_day"),
            "cycle_with": validated_data.pop("cycle_with"),
            "cycle_unit": validated_data.pop("cycle_unit")
        }
        calender = super().create(calneder_data)
        return calender