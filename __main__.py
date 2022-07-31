import time
import socket
from service import MinecraftWatcherService

def main():
    service = MinecraftWatcherService()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        service.start()

        while service.is_alive():
            if service.mc_stopped:
                client_socket.bind('127.0.0.1', port=25565)
                client_socket.listen()
                waiting = True
                while waiting:
                    print(f"Listening for connections: {client_socket.recv(100)}")
                    time.sleep(5)
            
            time.sleep(5)

        service.join()
    finally:
        print('Stopping... ')
        service.stop()
        service.join()
        exit(0)


if __name__ == '__main__':
    main()
    