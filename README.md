# vue-chartjs-prometheus

This repo will contain some exercises to use Vue3 with ChartJS and Prometheus.

## Prerequisites

The following tools should be installed on your local development environment:

- Docker
- Python & pip
- Node & npm

## Usage

In the main project folder:

```bash
docker-compose up --build
```

## Backend

```python
http://localhost:8000
```

## Frontend

```python
http://localhost:8001
```

## Prometheus Metrics Endpoint

```python
http://localhost:8000/metrics
```

## Prometheus Server Dashboard

```python
http://localhost:9090
```

## Run manually

- Backend

```python
# Path: vue-chartjs-prometheus/backend/chartjs
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

- Frontend 

```python
# Path: vue-chartjs-prometheus/frontend/chartjs_app
npm install
npm run dev -- --port 8001
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
