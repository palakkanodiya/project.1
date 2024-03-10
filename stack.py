class stack:
    def __init__(stack):
        stack.top = -1
        stack.stack_length = int(input("ENTER THE LENGTH OF THE STACK : "))
        stack.arr = [0] * stack.stack_length

    def menu(stack):
        flag=True
        while(flag):
            print('''_______MENU________
1.PUSH
2.POP
3.CHANGE
4.PEEK (look for top element)
5.DISPLAY STACK
6.TERMINATE THE PROGRAM
    ''')
            operation = int(input("ENTER OPERATION NUMBER : "))
            match (operation):
                case 1:
                    stack.push()   
                case 2:
                    stack.pop()
                case 3:
                    stack.change_value()
                case 4:
                    stack.peek_stack()
                case 5:
                    stack.display_stack()
                case 6:
                    print('BYE')
                    flag=False
            if operation<1 or operation>6:
                    print('NOTE :: WRONG OPERATION, PLEASE TRY AGAIN\n')

    def check_overflow(stack):
        if stack.top==stack.stack_length-1:
            print('NOTE :: OVERFLOW\n')
            return 1
        else:
            return 0
        
    def check_underflow(stack):
        if stack.top == -1:
            print('NOTE :: UNDERFLOW\n')
            return 1
        else:
            return 0
        

    def push(stack):
        if stack.check_overflow():
            return
        else:
            item = input("ENTER ELEMENT : ")
            stack.top += 1
            stack.arr[stack.top] = item
            print("RESULT :: ELEMENT INSERTED SUCCESSFULLY\n")
            return

    def pop(stack):
        if stack.check_underflow():
            return
        else:
            print("RESULT :: ELEMENT POPPED = ",stack.arr[stack.top],"\n")
            print()
            stack.arr[stack.top] = 0
            stack.top -= 1
            return

    def change_value(stack):
        if stack.check_underflow():
            return
        pos = int(input("ENTER INDEX OF ELEMENT TO BE CHANGED :  "))
        if pos > stack.top:
            print("NOTE :: THERE IS NO ELEMENT ON THAT INDEX\n")
            return
        element = input("ENTER NEW ELEMENT : ")
        stack.arr[pos] = element
        print("RESULT :: ELEMENT CHANGED SUCCESSFULLY\n")
        return
        
    def peek_stack(stack):
        if stack.check_underflow():
            return
        print('RESULT :: TOP ELEMENT IS = ',stack.arr[stack.top],"\n")
        return
    
    def display_stack(stack):
        print("RESULT :: ", stack.arr,"\n")
        return
        
stack = stack()
stack.menu()
