from rest_framework import serializers
from api.models import dataform



class DataFormserializers(serializers.ModelSerializer):
    class Meta:
        model = dataform
        #fields = ['name', 'email','city']
        fields = '__all__'


'''class DataFormserializers(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=40)
    city = serializers.CharField(max_length=20)
    date = serializers.DateTimeField()

    def create(self,validate_data):
        return dataform.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.email = validate_data.get('email',instance.email)
        instance.city = validate_data.get('city',instance.city)
        instance.date = validate_data.get('data',instance.date)
        instance.save()
        return instance'''