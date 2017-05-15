from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from app_noiseapi.models import Noise

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Noise
		fields = ('dong', 'ho', 'noise_data',)

class noise_api(GenericAPIView, 
				mixins.ListModelMixin,
				mixins.CreateModelMixin,
				mixins.UpdateModelMixin):

	queryset = Noise.objects.order_by('-noise_data')[:10]
	serializer_class = PostSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		req_dong, req_ho, req_noise = serializer.data['dong'], serializer.data['ho'], serializer.data['noise_data']
	
		query = Noise.objects.filter(dong=req_dong, ho=req_ho)
		if query:
			query[0].noise_data = req_noise
			query[0].save()

			return self.list(request, *args, **kwargs)
		else:
			return self.create(request, *args, **kwargs)
