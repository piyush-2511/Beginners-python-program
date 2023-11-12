#STACK
def push(val):
    a.append(val)
    print('Element pushed successfully')

def pop(a):
    val = a.pop()
    print('Popped item is : ',val)

def peek(a):
    top = len(a)-1
    print('Peek element : ',a[top])

def display(a):
    top = len(a)-1
    for i in range(top,-1,-1):
        print(a[i])



#linking

a = []
while True:
    choice = int(input('1-->Push \n2-->Poop \n3-->Peek \n4-->Display \nEnter the choice : '))
    if choice == 1:
        val = int(input('Enter no. to Push : '))
        push(val)
    elif choice == 2:
        if len(a) == 0:
            print('Empty Stack')
        else:
            pop(a)
    elif choice == 3:
        if len(a) == 0:
            print('Empty Stack')
        else:
            peek(a)
    elif choice == 4:
        if len(a) == 0:
            print('Empty Stack')
        else:
            display(a)
    else:
        break
