# Load Test Demo

## Іске қосу
pip install -r requirements.txt
uvicorn main:app --port 8000

## Эндпоинттер
- GET /
- GET /users
- GET /health

## Жүктемелік тестілеу
locust -f locustfile.py --host=http://localhost:8000