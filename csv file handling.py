#CSV file handling

import csv
def write():
    with open('details.csv','w') as obj:
        fobj = csv.writer(obj)
        fobj.writerow(['ROLL NO.','NAME','TOTAL MARKS'])
        while True:
            roll = int(input('etner roll no. : '))
            name = input('enter name : ')
            total = int(input('enter total marks : '))
            record = [roll,name,total]
            fobj.writerow(record)
            ch = int(input('1-->Enter more \n2-->Exit \nEnter your choice : '))
            if ch == 2:
                break

def display():
    with open('details.csv','r') as obj:
        fobj = csv.reader(obj)
        for i in fobj:
            print(i)

def search():
    with open('details.csv','r') as obj:
        fobj = csv.reader(obj)
        next(fobj)
        for i in fobj:
            if i[2]>=50:
                print(i)
                
display()



