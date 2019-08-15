# Creator: Garfield Grant       
# Creator: Horraine Mccalla     
# COMP1127 project
# Abstract data type file for the project


# This function creates a new queue data structure, with a tag 
def new_Queue():
    return ("Queue",[])


# This function checks to see if the arguement is a queue data structure or not
def is_Queue(queue):
    return type(queue)==tuple and len(queue)==2 and queue[0]=="Queue" and type(queue[1])==list


# This function return the contents(elements) in the queue data structure  
def queue_Contents(queue):
    if is_Queue(queue):
        return queue[1]
    else:
        return TypeError ("Not a Queue")

#This function checks to see if a queue entered as a arguement is empty
def empty_Queue(queue):
    return queue== new_Queue()


# This function returns the first element in the contents of the queue data structure
def queue_Front(queue):
    if not empty_Queue(queue):
        return queue_Contents(queue)[0]
    else:
        raise IndexError (queue, "Is empty no front element")
    
# This function adds an element to the back of the queue
def enqueue(queue,element):
    if is_Queue(queue):
        queue_Contents(queue).append(element)
    else:
        raise TypeError(queue, "Is not a Queue")

    
# This function remove the first element in the queue contents
def dequeue(queue):
    if not empty_Queue(queue):
        queue=queue_Contents(queue).pop(0)
        return queue
    else:
        raise IndexError (queue,"Queue has no element")








    

# This function creates a new stack data structure, with a tag. 
def new_Stack():
    return ("Stack",[])


# This function checks to see if the arguement has a stack data structure or not
def is_Stack(stack):
    return type(stack)==tuple and len(stack)==2 and stack[0]=="Stack" and type (stack[1])==list


# This function return the contents(elements) in the stack data structure  
def stack_Contents(stack):
    if is_Stack(stack):
        return stack[1]
    else:
        raise TypeError("Not a stack")

#This function checks to see if a stack entered as a arguement is empty
def empty_Stack(stack):
    return stack== new_Stack()


# This function returns the first element in the contents of the stack data structure
def stack_Top(stack):
    if not empty_Stack(stack):
        return stack_Contents(stack)[0]
    else:
        raise IndexError (stack, "Is a empty stack")

    
# This function add elements to the first position (index 0) of the stack contents 
def push (stack,element):
    if is_Stack(stack):
        stack=stack_Contents(stack).insert(0,element)
        return stack
    else:
        raise TypeError(stack,"Is not a stack")
    

# This function remove the last element entered in the stack contents, hence last in first out.
def pop(stack):
    if not empty_Stack(stack):
        stack=stack_Contents(stack).pop(0)
        return stack
    else:
        raise TypeError (stack, "Not a stack")

