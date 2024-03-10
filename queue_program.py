class queue:
    def __init__(queue):
        queue.queue_length = int(input("ENTER THE LENGTH OF THE QUEUE : "))
        queue.arr = [0]*queue.queue_length
        queue.front = -1
        queue.rear = -1

    def menu(queue):
        flag=True
        while(flag):
            print('''______MENU________
1.ENQUEUE
2.DEQUEUE
3.CHANGE
4.PEEK (look for the element at front)
5.DISPLAY THE QUEUE
6.TERMINATE THE PROGRAM
    ''')
            operation = int(input("ENTER OPERATION NUMBER : "))
            match (operation):
                case 1:
                    queue.enqueue()
                case 2:
                    queue.dequeue()
                case 3:
                    queue.change_q()
                case 4:
                    queue.peek_q()
                case 5:
                    queue.display_q()
                case 6:
                    print('BYE')
                    flag=False
            if operation>6 or operation<1:
                print('NOTE :: WRONG OPERATION, PLEASE TRY AGAIN\n')
        
    def is_full(queue):
        if queue.front==0 and queue.rear==queue.queue_length-1:
            print("NOTE :: OVERFLOW\n")
            return 1
        else:
            return 0

    def is_empty(queue):
        if queue.front==-1 and queue.rear==-1:
            print("NOTE :: UNDERFLOW\n")
            return 1
        else:
            return 0   
    
    def enqueue(queue):
        if queue.is_full():
            return
        if queue.front == -1:
            queue.front=0
        queue.rear+=1
        item = input("ENTER ELEMENT : ")
        queue.arr[queue.rear]=item
        print("RESULT :: ELEMENT INSERTED SUCCESSFULLY\n")
        
    def dequeue(queue):
        if queue.is_empty():
            return
        print("RESULT :: ELEMENT REMOVED = ",queue.arr[queue.front],"\n")
        queue.arr[queue.front]=0
        if queue.front == queue.rear:            
            queue.front=-1
            queue.rear=-1
        else:
            queue.front+=1

    def change_q(queue):
        if queue.is_empty():
            return
        pos = int(input("ENTER INDEX OF ELMENT TO BE CHANGED : "))
        if pos < queue.front or pos > queue.rear:
            print("NOTE :: THERE IS NO ELEMENT ON THAT INDEX\n")
            return
        element = input("ENTER NEW ELEMENT : ")
        queue.arr[pos]=element
        print("RESULT :: ELEMENT CHANGED SUCCESSFULLY\n")

    def peek_q(queue):
        if queue.is_empty():
            return
        print("RESULT :: TOP ELEMENT IS = ", queue.arr[queue.front], "\n")    
        
    def display_q(queue):
        print("RESULT :: ", queue.arr, "\n")
        print()                        

queue = queue()
queue.menu()
