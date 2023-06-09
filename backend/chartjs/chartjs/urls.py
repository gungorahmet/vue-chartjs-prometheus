"""
URL configuration for chartjs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from metric.views import HelloWorldDataView, GetDumbDataLineChartView, GetDumbDataDoughnutChartView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api/v1/helloworld', HelloWorldDataView.as_view()),
    path('api/v1/get_dumb_line_chart_data', GetDumbDataLineChartView.as_view()),
    path('api/v1/get_dumb_doughnut_chart_data', GetDumbDataDoughnutChartView.as_view()),
    path('', include('django_prometheus.urls')),
]

urlpatterns += staticfiles_urlpatterns()