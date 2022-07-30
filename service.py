from threading import Thread
import time
import docker
from utils import get_running_containers

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
            print(f"Currently running containers: {get_running_containers()}.")
            time.sleep(self.pooling_interval)

    def stop(self):
        print('Service stopped')
        self.running = False
