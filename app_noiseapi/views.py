from django.shortcuts import render
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from app_noiseapi.models import Noise

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Noise
		fields = '__all__'

class noise_api(GenericAPIView, mixins.ListModelMixin):
	queryset = Noise.objects.all()
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

