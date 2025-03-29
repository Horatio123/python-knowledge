import threading
import time


def start_thread():
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()


def worker():
    while True:
        id = threading.get_ident()
        print(f"worker is work, id is {id}")
        time.sleep(3)


if __name__ == "__main__":
    start_thread()
    while True:
        print("main is work")
        time.sleep(100)
