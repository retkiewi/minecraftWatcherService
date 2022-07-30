from threading import Thread
import time
from utils import isPortTaken

class Service(Thread):
    def __init__(self, port=25565, pooling_interval=10):
        super().__init__()
        self.running = False
        self.port = port
        self.pooling_interval = pooling_interval

    def run(self):
        print('Service started')
        self.running = True

        while self.running:
            print(f"Port {self.port} is currently {'taken' if isPortTaken(self.port) else 'open'}.")
            time.sleep(self.pooling_interval)

    def stop(self):
        print('Service stopped')
        self.running = False
