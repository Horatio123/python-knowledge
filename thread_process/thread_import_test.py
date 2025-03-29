import time
from thread2import import start_thread


if __name__ == '__main__':
    start_thread()
    while True:
        print("thread_import_test is running")
        time.sleep(100)
    