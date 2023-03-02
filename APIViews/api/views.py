from django.forms import model_to_dict
from .serializers import MenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Men

class MenAPIView(APIView):
    def get(self,request):
        lst = Men.objects.all().values()
        return Response({'posts':MenSerializer(lst,many=True).data})

    def post(self, request):
        serializer = MenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def create(self, validated_data):
        return Men.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance

    def put(self,request, *args,**kwargs):
        pk = kwargs.get('pk',None)
        if not pk:
            return Response({'error': 'Method Put Not Allowed'})

        try:
            instance = Men.objects.get(pk=pk)
        except:
            return Response({'error':'Object does not  exists'})

        serializers = MenSerializer(data=request.data, instance=instance)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({'post':serializers.data})
    def delete(self,request,*args,**kwargs):
        pk= kwargs.get('pk',None)
        if not pk:
            return Response({'error':'Method Delete not allowed'})

        w = Men.objects.get(pk=pk)
        w.delete()

        return Response({'post':'delete post' + str(pk)})
