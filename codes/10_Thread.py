from threading import Thread, Semaphore
import time


def thread_function(number):
    print("Sleeping for 5 second from thread %d\n" % number)
    time.sleep(5)
    print("Finished sleeping from thread % d\n" % number)


for i in range(5):
    new_thread = Thread(target=thread_function, args=(i,))
    # new_thread.start()


# another sample
class Vars:
    var = 0

    def __init__(self):
        pass


def thread_function2(num):
    # sem.acquire()
    print("thread %d, before increment: current value: %d\n" % (num, Vars.var))
    time.sleep(5)
    Vars.var += 1
    print("thread %d, after increment: current value: %d\n" % (num, Vars.var))
    # sem.release()

thread1 = Thread(target=thread_function2, args=(1,))
thread2 = Thread(target=thread_function2, args=(2,))
thread3 = Thread(target=thread_function2, args=(3,))
thread4 = Thread(target=thread_function2, args=(4,))
thread5 = Thread(target=thread_function2, args=(5,))

sem = Semaphore(1)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
