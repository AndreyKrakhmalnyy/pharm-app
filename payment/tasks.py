from core.celery.celery import app

@app.task
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)   