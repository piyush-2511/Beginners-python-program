#BINARY FILE HANDLING


import pickle
#writing
def write():
    with open('myfile.dat','wb') as f:
        list1=['ram','sita','gita']
        pickle.dump(list1,f)

#reading
def read():
    with open('myfile.dat','rb') as f:
        list1=pickle.load(f)
        print(list1)
'''
#wrting nested list in binary file
def nestwrite():
    with open('myfile.dat','wb') as f:
        record = []
        while True:
            roll = int(input('Enter roll no. : '))
            name = input('Enter name : ')
            marks = int(input('Enter marks : '))
            list1=[roll,name,marks]
            record.append(list1)
            ch = int(input('1-->Enter more \n2-->Exit \nEnter choice : '))
            if ch == 2:
                break
'''            

#searching

def search():
    with open('myfile.dat','rb') as f:
        roll = int(input('Enter roll no. to search : '))
        flag = 0
        r = pickle.load(f)
        for i in r:
            if i[0]==roll:
                print(i)
                flag = 1
                break
            if flag == 0:
                print('Roll not found')

search()

