import time

class Producer:
    def produce(self):
        print("Producer is working hard.")

    def meet(self):
        print("Producer has time to meet you now.")

class Proxy:
    def __init__(self):
        self.occupied = True
        self.producer = None

    def produce(self):
        if not self.occupied:
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()
        else:
            time.sleep(2)
            print("producer is busy.")

p = Proxy()
p.produce()
p.occupied = False
p.produce()