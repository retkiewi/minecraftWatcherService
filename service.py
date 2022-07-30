from threading import Thread
import time
import docker
from utils import is_mc_stopped

class MinecraftWatcherService(Thread):
    def __init__(self, port=25565, pooling_interval=10):
        super().__init__()
        self.running = False
        self.port = port
        self.pooling_interval = pooling_interval
        self.mc_stopped = is_mc_stopped()

    def run(self):
        print('Service started')
        self.running = True

        while self.running:
            self.mc_stopped = is_mc_stopped()
            time.sleep(self.pooling_interval)

    def stop(self):
        print('Service stopped')
        self.running = False
