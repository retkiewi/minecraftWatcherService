import time
import socket
from service import MinecraftWatcherService

def main():
    service = MinecraftWatcherService()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 25565))
    
    try:
        service.start()

        while service.is_alive():
            print(client_socket.listen(1))
            
            time.sleep(5)

        service.join()
    finally:
        print('Stopping... ')
        service.stop()
        service.join()
        exit(0)


if __name__ == '__main__':
    main()
    