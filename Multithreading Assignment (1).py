#!/usr/bin/env python
# coding: utf-8

# Q-1 What is multithreading in python ? Name is it used ? Name the module used to handle threads in python.

# Ans-1 Mutithreading is used to achieve multitasking .Multithreading is defined as ability of a processor to execute multiple threading concurrently . multithreading facilitates sharing data space data space and resources of multiple threads with main thread . it allows efficint and easy communiction between the threads.
# Module use dto handle thread in python 
# start() used to initiate activity of thread 
# run() used to define thread's activity and can be overridden by a class that thread class.
# join() used to block execution of another code untill the thread terminates.

# Q-2 Why threading module used ? Write the use of the following function:
# 1. activecout()
# 2. Currentthread()
# 3. enumerate()

# Ans-2 Threading allows you to have different parts of your program run concurrently and can simplify your design .
#  
# 1. ACTIVECOUNT()- used to count the the currently active or running thread 
# syntax threading.activecount()
# 
# 2. CURRENTTHREAD()- it  is an inbuilt method of threading module, it is used to return the thread object ,which correspond to caller's thread of control.
# 
# 3. ENUMERATE()- used to add counter to an iterable and return it in form of enumerating object. enumerated object can thread used directly for loops or converted into list of tuples using list() function.

# Q-3 Explain the following functions:
# 1. run()
# 2. start()
# 3. join()
# 4. isAlive()

# Ans-3 
# 1. RUN()- it is used to the entry point for thread.
# 2. START()- It start the thread by calling the run method.
# 3. JOIN()- It wait for threads to terminate.
# 4. ISALIVE()- It is used to check weather a thread is still executing.

# Q-4 Write a python program to create two threads . Thread one must print the list of squares and thread two must print the list of cubes.

# In[5]:


import threading
def print_cube(num):
    print("cube:{}",format(num*num*num))
def print_square(num):
    print("square:{}",format(num*num))
    
if __name__=="__main__":
    t1=threading.Thread(target=print_square , args=(10,))
    t2=threading.Thread(target=print_cube, args=(10,))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")


# Q-5 State advantges and distadvantages of multithreading .

# Ans-5 
#  ADVANTAGE:
#           1. Enable efficient utilization of resouces as the thread shares the data space and memory.
#           2. Multithreading in python allow the concurrent and parallel occurence of various task.
#           3. it cause reduction in time consumption or response time by increasing the performance.
#           
# DISADVANTAGES:
#           1. Difficult in writing code.
#           2. Difficult of debugging.
#           3. Difficult of managing concurrency.

# Q-6 Explain deadlocks and race conditions.

# Ans-6 Deadlock:
#               Deadlock exist when two threads seek one lock simultaneously.
#       Race :
#             A race condition occurs when two threads use the same varible  at a given time.

# In[ ]:




