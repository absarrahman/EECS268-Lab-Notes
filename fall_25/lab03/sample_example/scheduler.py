
'''

This is just a hint for everyone. This is not the solution for the lab task.
NOTE:>> It is not required for you to follow this sample but it is for 
giving you an idea of the workflow of this lab

'''
# from linkedqueue import LinkedQueue
# from process import Process
# from node import Node

class Scheduler:
    def __init__(self):
        # initiate the linked queue
        # something like self.process_queue = LinkedQueue()
        pass

    # Responsible for starting a process
    def start_cmd(self, name):
        # create a process and enqueue it to your process queue
        pass

    # process at front of queue calls a function. That function gets added to the process' call stack
    def call_cmd(self, func, can_handle_except):
        
        # check whether the queue is empty or not. If it is empty then terminate the function

        # else you have to dequeue your process from your linked queue and store that process in a variable


        # since we have the process variable, we can add function to the process' func stack
        
        # moves the process to back of the queue

        # Once our function call is done we have to enqueue it back to the queue. We can easily do it since

        # we have the reference of the process
        pass

    
    # returns from the top function on the front of queue process
    def return_cmd(self):

        # logic is kinda similar to the call function

        # check whether the queue is empty or not. If it is empty then terminate the function
        
        # else you have to dequeue your process from your linked queue and store that process in a variable

        # pop the top function  from the process' function stack

        # if my top function is main the show the user that the process ended
        # else enqueue that process back of the queue
        pass



    # raises an exception in the front process of the queue
    def raise_cmd(self):
        # check whether the queue is empty or not. If it is empty then terminate the function

        # dequeue the front process of the queue and store that in a variable

        

        # add a loop. The loop will keep running until the process' call stack is empty. HINT: while call stack not empty
            # pop the top function from the call stack and store into a variable

            # if the function handles exception, show the user that the function handles exception
            # and enqueue the process back to the process linked queue and terminate this function

            # if the function name is main, show the process ended. Similar to the return function 
            # and terminate this function
        # removes process from linked queue
        pass
