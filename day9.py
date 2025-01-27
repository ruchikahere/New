# import threading
# print(threading.current_thread())

# print(threading.current_thread().is_alive())
# # How to create threads
# # first we import thread class from threading module
# from threading import Thread
# # creating a function containing code to be executed parallely
# # def display():
# #     for i in range(5):
# #         print("hello Everyone")
# # #creating new thread 
# # t1 = Thread(target=display)
# # # using start() method
# # t1.start()
# #Multithreading in python
# import threading


# # def print_cube(num):
# #     print("Cube: {}" .format(num * num * num))


# # def print_square(num):
# #     print("Square: {}" .format(num * num))


# # if __name__ =="__main__":
# #     t1 = threading.Thread(target=print_square, args=(10,))
# #     t2 = threading.Thread(target=print_cube, args=(10,))

# #     t1.start()
# #     t2.start()

# #     t1.join()
# #     t2.join()

# #     print("Done!")

# #also importing os module
# import threading
# import os

# def task1():
#     print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 1: {}".format(os.getpid()))

# def task2():
#     print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
#     print("ID of process running task 2: {}".format(os.getpid()))

# if __name__ == "__main__":

#     print("ID of process running main program: {}".format(os.getpid()))

#     print("Main thread name: {}".format(threading.current_thread().name))

#     t1 = threading.Thread(target=task1, name='t1')
#     t2 = threading.Thread(target=task2, name='t2')

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

# #Python threadpool  is a collection of threads that are created in advance and can be reused to execute multiple tasks.
# import concurrent.futures

# def worker():
#     print("Worker thread running")

# pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

# pool.submit(worker)
# pool.submit(worker)

# pool.shutdown(wait=True)

# print("Main thread continuing to run")

# from threading import Thread, current_thread
# def display():
#     for i in range(4):
#         print ("World hello")
# def show():
#     for i in range(3):
#         print("heyyy")

# t1 = Thread(target=display)
# t2 = Thread(target = show)
# t1.setName("Ruchika")
# print(t1.name)

# current_thread().name = "Anisha"
# print(current_thread().name)

# import threading 

# # global variable x 
# x = 0

# def increment(): 
# 	""" 
# 	function to increment global variable x 
# 	"""
# 	global x 
# 	x += 1

# def thread_task(): 
# 	""" 
# 	task for thread 
# 	calls increment function 100000 times. 
# 	"""
# 	for _ in range(100000): 
# 		increment() 

# def main_task(): 
# 	global x 
# 	# setting global variable x as 0 
# 	x = 0

# 	# creating threads 
# 	t1 = threading.Thread(target=thread_task) 
# 	t2 = threading.Thread(target=thread_task) 

# 	# start threads 
# 	t1.start() 
# 	t2.start() 

# 	# wait until threads finish their job 
# 	t1.join() 
# 	t2.join() 

# if __name__ == "__main__": 
# 	for i in range(10): 
# 		main_task() 
# 		print("Iteration {0}: x = {1}".format(i,x)) 

# import time

# def task1():
#     print("Task 1 start")
#     time.sleep(3)  # 3 seconds ke liye wait karega
#     print("Task 1 end")

# def task2():
#     print("Task 2 start")
#     time.sleep(3)
#     print("Task 2 end")

# # Dono tasks ko sequentially run karte hain
# task1()
# task2()

# 
# import threading
# import time

# def greet(name, delay):
#     print(f"Hello, {name}!")
#     time.sleep(delay)
#     print(f"Goodbye, {name}!")

# # Threads with arguments
# t1 = threading.Thread(target=greet, args=("Alice", 2))
# t2 = threading.Thread(target=greet, args=("Bob", 3))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# Threading mein Synchronization
# Jab multiple threads ek shared resource (jaise list, file, etc.) ko access karte hain, toh synchronization zaroori hoti hai.

# import threading

# counter = 0
# lock = threading.Lock()

# def increment():
#     global counter
#     for _ in range(100000):
#         with lock:  # Ensure only one thread accesses this block at a time
#             counter += 1

# # Create threads
# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Final counter value:", counter)


try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")
