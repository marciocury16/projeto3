from rest_framework import  viewsets
from .models import fruit
from frexco.serializer import fruitSerializer
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

class fruitViewSet(viewsets.ModelViewSet):
    queryset = fruit.objects.all()
    serializer_class = fruitSerializer

@api_view(['GET', 'POST', 'DELETE'])
def fruit_list(request):
    if request.method == 'GET':
        fruit = fruit.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            fruit = fruit.filter(title__icontains=title)
        
        fruit_serializer = fruitSerializer(fruit, many=True)
        return JsonResponse(fruit_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        fruit_data = JSONParser().parse(request)
        fruit_serializer = fruitSerializer(data=fruit_data)
        if fruit_serializer.is_valid():
            fruit_serializer.save()
            return JsonResponse(fruit_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(fruit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = fruit.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try: 
        fruit = fruit.objects.get(pk=pk) 
    except fruit.DoesNotExist: 
        return JsonResponse({'message': 'The fruit does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        fruit_serializer = fruitSerializer(fruit) 
        return JsonResponse(fruit_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        fruit_serializer = fruitSerializer(fruit, data=tutorial_data) 
        if fruit_serializer.is_valid(): 
            fruit_serializer.save() 
            return JsonResponse(fruit_serializer.data) 
        return JsonResponse(fruit_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        fruit.delete() 
        return JsonResponse({'message': 'fruit was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def fruit_list_published(request):
    fruit = fruit.objects.filter(published=True)
        
    if request.method == 'GET': 
        fruit_serializer = fruitSerializer(fruit, many=True)
        return JsonResponse(fruit_serializer.data, safe=False)