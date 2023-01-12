from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Review_Management.models import ReviewMedia
from .serializers import ReviewMediaSerializer


class ReviewMediaList(APIView):
    def get(self, request):
        model = ReviewMedia.objects.all()
        serializer = ReviewMediaSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewMediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewMediaDetails(APIView):
    def get(self, request, project):
        try:
            model = ReviewMedia.objects.get(id=project)
        except ReviewMedia.DoesNotExist:
            return Response(f'ReviewMedia with {project} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewMediaSerializer(model)
        return Response(serializer.data)

    def put(self, request, project):
        try:
            model = ReviewMedia.objects.get(id=project)
        except ReviewMedia.DoesNotExist:
            return Response(f'ReviewMedia with {project} is Not Found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewMediaSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
