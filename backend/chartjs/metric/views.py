import random

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorldDataView(APIView):
    def get(self, request):
        data = {
            'message': 'Hello, world!'
        }
        return Response(data)

class GetDumbDataLineChartView(APIView):
    def get(self, request):
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
        option = request.query_params.get('option', None)  # It's a string

        if not option:
            data = [10, 30, 40, 20]
        elif option == "1":
            data = [60, 10, 15, 15]
        elif option == "2":
            data = [40, 30, 20, 10]
        elif option == "3":
            data = [25, 25, 25, 25]
        else:
            data = [70, 10, 15, 5]

        response = {
            'chart': {
                'chartData': {
                    'labels': ['Python', 'VueJs', 'TypeScript', 'JavaScript'],
                    'datasets': [ 
                                    {
                                    'backgroundColor': ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0'],
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
