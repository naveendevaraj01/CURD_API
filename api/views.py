from django.shortcuts import render
from api.models import dataform
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from api.serializers import DataFormserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404



class dataformModelViewset(viewsets.ModelViewSet):
    serializer_class = DataFormserializers
    queryset = dataform.objects.all()



class dataformGenericVeiwset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = DataFormserializers
    queryset = dataform.objects.all()



class dataformVeiwset(viewsets.ViewSet):
    def list(self, request):
        obj = dataform.objects.all()
        serializer=DataFormserializers(obj,many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer=DataFormserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def retrieve(self, request, pk=None):
        queryset = dataform.objects.all()
        obj = get_object_or_404(queryset,pk=pk)
        serializer=DataFormserializers(obj)
        return Response(serializer.data)    

    def update(self, request,pk=None):
        obj = dataform.objects.get(pk=pk)
        serializer = DataFormserializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class genericAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = DataFormserializers
    queryset = dataform.objects.all()
    lookup_field = 'id'
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request,id)



class dataformAPIView(GenericAPIView):
    serializer_class=DataFormserializers
    def get(self, request):
        obj = dataform.objects.all()
        serializer=DataFormserializers(obj,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=DataFormserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class dataformDetails(GenericAPIView):
    serializer_class=DataFormserializers
    def get_object(self, id):
        try:
            return dataform.objects.get(id=id)
        except dataform.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        obj = self.get_object(id)
        serializer = DataFormserializers(obj)
        return Response(serializer.data)

    def put(self,request,id):
        obj = self.get_object(id)
        serializer = DataFormserializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        obj = self.get_object(id)
        obj.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def name_list(request):
    if request.method == 'GET':
        obj = dataform.objects.all()
        serializer=DataFormserializers(obj,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer=DataFormserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def name_details(request,id):
    try:
        obj = dataform.objects.get(id=id)
    except dataform.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DataFormserializers(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DataFormserializers(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)