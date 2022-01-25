from rest_framework import  viewsets
from .models import region, fruit
from .serializer import regionSerializer, fruitSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response




class regionViewSet(viewsets.ModelViewSet):
    queryset = region.objects.all()
    serializer_class = regionSerializer

class fruitViewSet(viewsets.ModelViewSet):
    queryset = fruit.objects.all()
    serializer_class = fruitSerializer   
   
    def get(self, request, format=None):
        snippets = fruit.objects.all()
        serializer = fruitSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = fruitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class fruitDetail(APIView):
   
    def get_object(self, pk):
        try:
            return fruitSerializer.objects.get(pk=pk)
        except fruitSerializer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = fruitSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = fruitSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class fruitList (mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = fruit.objects.all()
    serializer_class = fruitSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class fruitDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = fruit.objects.all()
    serializer_class = fruitSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

