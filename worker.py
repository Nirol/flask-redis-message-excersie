from rq import Worker, Queue, Connection
import redis


listen = ['default']
conn = redis.Redis()

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()