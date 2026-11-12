from datetime import datetime

from events.models import Event

from rest_framework import serializers
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields="__all__"
        read_only_fields=["organizer","created_at"]

    def validate(self,data):
        date=data.get("date")
        todays_date = datetime.today().date()
        #todays_date_time=datetime.today().time()

        # year=datetime.today().year
        # month=datetime.today().month
        # day=datetime.today().day
        if date<todays_date:
            raise serializers.ValidationError("Invalid date")
        return data