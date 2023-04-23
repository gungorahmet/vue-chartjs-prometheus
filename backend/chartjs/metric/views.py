import random

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorldDataView(APIView):
    def get(self, request):
        data = {
            'message': 'Hello, world!'
        }
        return Response(data)

class GetDumbDataView(APIView):
    def get(self, request):
        random_data = []
        times = []
        for i in range(60):
            time = "10:{:02d}".format(i)
            times.append(time)

        for i in range(61):
            random_data.append(random.uniform(95, 100))

        response = {
            'chart': {
                'chartData': {
                    'labels': times,
                    'datasets': [ { 'label': 'Uptime per minute',
                                    'data': random_data,
                                    'borderColor': '#36A2EB',
                                    'backgroundColor': '#9BD0F5', } ]
                },
                'chartOptions': {
                    'responsive': True,
                    'scales': {
                        'y': {
                            'suggestedMin': 0,
                            'suggestedMax': 100
                        }
                    }
                }
            }
        }
        return Response(response)
