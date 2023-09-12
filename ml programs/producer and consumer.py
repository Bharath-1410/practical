import threading
import time
import random

buffer = []
maxSize = 10
mutex = threading.Semaphore(1)
empty = threading.Semaphore(maxSize)
full = threading.Semaphore(0)


class ProducerThread(threading.Thread):
    def run(self):
        global buffer
        while True:
            item = random.randint(1,100)
            empty.acquire()
            mutex.acquire()
            buffer.append(item)
            print("producer produced:" , item)
            mutex.release()
            full.release()
            time.sleep(random.random())

class ConsumerThread(threading.Thread):
    def run(self):
        global buffer
        while True:
            full.acquire()
            mutex.acquire()
            item = buffer.pop(0)
            print("Consumer consumed:", item)
            mutex.release()
            empty.release()
            time.sleep(random.random())
            
producer = ProducerThread()
consumer = ConsumerThread()
producer.start()
consumer.start()

producer.join()
consumer.join()
print('done!')

            