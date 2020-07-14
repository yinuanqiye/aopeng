from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import goods
from aopeng_sites.serializers import goodsSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    @csrf_exempt
    def goods_list(request):
        if request.method == 'GET':
            goodsList = goods.objects.all()
            serializer = goodsSerializer(goodsList, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = goodsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def goods_detail(request, pk):
        try:
            onegoods = goods.objects.get(pk=pk)
        except goods.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = goodsSerializer(onegoods)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = goodsSerializer(goods, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            goods.delete()
            return HttpResponse(status=204)

