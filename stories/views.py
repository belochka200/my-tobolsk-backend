from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone

from .models import Story
from .serializers import StorySerializer


class StoriesViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(methods=['get'], detail=False)
    def today(self, request):
        stories = Story.objects.filter(
            date__day=timezone.now().day).order_by('-time')
        serializer = self.get_serializer(stories, many=True)
        return Response(serializer.data)

    # @action(methods=['get'], detail=False)
    # def thisweek(self, request):
    #     today = timezone.now().day
    #     stories = Story.objects.all()
    #     ...
