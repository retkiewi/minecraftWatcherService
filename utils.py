import socket
import docker
from contextlib import closing

def isPortTaken(port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        return sock.connect_ex(('127.0.0.1', port)) == 1

def is_mc_stopped():
    client = docker.from_env()
    return client.containers.list(all=True, filters={'name': 'mc'})[0].status == 'exited'

def start_mc_container():
    client = docker.from_env()
    client.containers.list(filters={'name': 'mc'})[0].start()
