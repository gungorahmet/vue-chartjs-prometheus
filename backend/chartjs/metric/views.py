import random

from rest_framework.views import APIView
from rest_framework.response import Response

from prometheus_client import Gauge, Counter

request_count_line_chart_metric = Gauge('request_count_line_chart_metric', 'HTTP GET Request count of Line Chart')
request_count_doughnut_chart_metric = Counter('request_count_doughnut_chart_metric', 'HTTP GET  Request count of Doughnut Chart')

class HelloWorldDataView(APIView):
    def get(self, request):
        data = {
            'message': 'Hello, world!'
        }
        return Response(data)

class GetDumbDataLineChartView(APIView):
    def get(self, request):
        request_count_line_chart_metric.inc()

        option = request.query_params.get('option', None)  # It's a string

        random_data = []
        times = []
        for i in range(60):
            time = "10:{:02d}".format(i)
            times.append(time)

        if not option:
            min_rand_val = 0
            max_rand_val = 9
        elif option == "1":
            min_rand_val = 10
            max_rand_val = 19
        elif option == "2":
            min_rand_val = 20
            max_rand_val = 29
        elif option == "3":
            min_rand_val = 30
            max_rand_val = 39
        else:
            min_rand_val = 95
            max_rand_val = 100

        for i in range(61):
            random_data.append(random.uniform(min_rand_val, max_rand_val))

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


class GetDumbDataDoughnutChartView(APIView):
    def get(self, request):
        request_count_doughnut_chart_metric.inc()

        option = request.query_params.get('option', None)  # It's a string

        if not option:
            data = [50, 50]
        elif option == "1":
            data = [99.98, 0.02]
        elif option == "2":
            data = [60.01, 39.99]
        elif option == "3":
            data = [35.52, 64.48]
        else:
            data = [90.12, 9.88]

        response = {
            'chart': {
                'chartData': {
                    'labels': ['Up', 'Down'],
                    'datasets': [ 
                                    {
                                    'backgroundColor': ['#36A2EB', '#FF6384'],
                                    'data': data
                                    }
                                ]
                },
                'chartOptions': {
                    'responsive': True,
                }
            }
        }
        return Response(response)
