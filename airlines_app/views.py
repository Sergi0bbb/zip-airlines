from rest_framework import viewsets, status
from rest_framework.response import Response

from airlines_app.models import Airplane
from airlines_app.serializers import (
    AirplaneSerializer,
    AirplaneDetailSerializer
)


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneSerializer
        if self.action == "retrieve":
            return AirplaneDetailSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        data = request.data
        if len(data) > 10:
            return Response(
                {"error ": "You can create only 10 airplanes!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AirplaneSerializer(data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Airplanes created!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
