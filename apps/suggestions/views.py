from datetime import datetime
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import AllowAny
from apps.events.models import Event
from .models import Suggestion
from .serializers import SuggestionSerializer


def is_event_running(event: Event):
    now = datetime.today().isoformat()
    start_date = event.start_date.iso_format()
    finish_date = event.finish_date.iso_format()
    return start_date < now < finish_date


class SuggestionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet
):
    permission_classes = (AllowAny,)
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer

    def create(self, request, *args, **kwargs):
        serializer = SuggestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        event = Event.objects.get(id=serializer.validated_data.get("event"))

        if event is None:
            raise ValidationError("Este evento no existe")

        # TODO check the user has a ticket for this event

        if not is_event_running():
            raise ValidationError("No se pueden sugerir canciones para este eventop")

        existing_suggestion = Suggestion.objects.get(
            user=request.user,
            event=event
        )

        if existing_suggestion is not None:
            raise PermissionDenied("Ya has sugerido una canción para este evento")

        suggestion = serializer.save()
        return Response(serializer.data)


"""
class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request):
        an_apiview = [
            'indica tu canción a elegir',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'la canción indicada es: {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
"""
