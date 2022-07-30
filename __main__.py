import time
from service import Service

def main():
    service = Service()
    
    try:
        service.start()

        while service.is_alive():
            time.sleep(5)

        service.join()
    finally:
        print('Stopping... ')
        service.stop()
        service.join()
        exit(0)


if __name__ == '__main__':
    main()
    