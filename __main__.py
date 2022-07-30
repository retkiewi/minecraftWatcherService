import time
from service import Service

def main():
    service = Service()
    
    try:
        service.start()

        while service.is_alive():
            time.sleep(60)

        service.join()
        
    finally:
        service.stop()
        service.join()


if __name__ == '__main__':
    main()
    