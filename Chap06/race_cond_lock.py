import threading

x = 0  # global variable shared by threads

def increment():
    global x
    x+= 1

def thread_task(lock):
    for _ in range(300000):
        # Acquire lock befor accessing the shared data
        lock.acquire()  
        increment()
        # Release lock after finishing the race
        lock.release()

def main_task():
    global x
    x = 0     # initialize x as 0

    lock = threading.Lock()    # create a lock object

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main_task()
    print('Iteration {0}: x = {1}'.format(i, x))
