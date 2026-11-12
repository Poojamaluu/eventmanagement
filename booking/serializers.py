from rest_framework import serializers

from booking.models import Booking
from events.models import Event


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'
        read_only_fields=['user','amount','status','created_at']

    def validate(self, data):
        event=data['event']
        seats=data['seats']
        if event.available_seats<seats:
            raise serializers.ValidationError('Seats are not available')
        return data