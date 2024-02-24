from core.celery.celery import app


@app.task
def sum_quad(x, y):
    return x ** 2 + y ** 2
