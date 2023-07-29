import concurrent.futures
import queue
import threading
import time

"""
https://www.cnblogs.com/lincappu/p/12890761.html
https://www.geeksforgeeks.org/queue-in-python/
https://www.geeksforgeeks.org/multithreading-python-set-1/
https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
"""

def play_queue():
    q = queue.Queue()

    q.put('sss')
    q.put('aaa')
    q.put('xxx')

    for _ in range(q.qsize()):
        print(q.get())
        print('xxx')
        q.task_done()
        print('yyy')
    q.join()
    print('zzz')


def work(work_queue):
    while not work_queue.empty():
        print(work_queue.get(), threading.current_thread().name)
        time.sleep(3)
        work_queue.task_done()


def play_thread():
    q = queue.Queue()
    q.put('sss')
    q.put('aaa')
    q.put('xxx')
    q.put('ccc')
    q.put('vvv')
    q.put('bbb')

    t1 = threading.Thread(target=work, args=(q,))
    t2 = threading.Thread(target=work, args=(q,))
    t1.start()
    t2.start()

    q.join()
    print('q is finished')

    t1.join()
    print('t1 is finished')
    t2.join()
    print('t2 is finished')


def work2(*lll):
    print(lll, threading.current_thread().name)
    time.sleep(2)


def play_pool():
    print("Worker thread running")

    # create a thread pool with 2 threads
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

    ll = ['11', '22', '33']

    # submit tasks to the pool
    pool.submit(work2, *ll)
    pool.submit(work2, '222')
    pool.submit(work2, '111')
    pool.submit(work2, '333')
    pool.submit(work2, '444')
    pool.submit(work2, '555')

    # wait for all tasks to complete
    pool.shutdown(wait=True)

    print("Main thread continuing to run")


def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1


def thread_task_no_syn():
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        increment()


def thread_task_syn(lock):
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()


def play_thread_no_syn():
    global x
    # setting global variable x as 0
    x = 0

    # creating threads
    t1 = threading.Thread(target=thread_task_no_syn())
    t2 = threading.Thread(target=thread_task_no_syn())

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


def play_thread_syn():
    global x
    # setting global variable x as 0
    x = 0

    # creating a lock
    lock = threading.Lock()

    # creating threads
    t1 = threading.Thread(target=thread_task_syn, args=(lock,))
    t2 = threading.Thread(target=thread_task_syn, args=(lock,))

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


if __name__ == '__main__':
    # play_queue()
    # play_thread()
    # play_pool()
    global x
    for i in range(10):
        # play_thread_no_syn()
        play_thread_syn()
        print("Iteration {0}: x = {1}".format(i, x))
