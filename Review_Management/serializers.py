from rest_framework import serializers
from Review_Management.models import ReviewMedia


class ReviewMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewMedia
        fields = '__all__'
