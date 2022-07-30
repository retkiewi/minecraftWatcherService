import socket
import docker
from contextlib import closing

def isPortTaken(port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        return sock.connect_ex(('127.0.0.1', port)) == 1


def get_running_containers():
    client = docker.from_env()
    return client.containers.list(filters={'status': 'running'})

def start_mc_container(port=25565):
    client = docker.from_env()
    client.containers.list(filters={'status': 'stopped', 'name': 'mc'})[0].start()
