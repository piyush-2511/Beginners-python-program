#FILE HANDLING
'''
"r" - open a file for reading
"w" - open a file for writing
"x" - create a file if not exits
"a" - add more content to a file
"t" - text mode
"b" - binary mode
"+" - read and write
'''
#f = open("piyush.txt",'r')
#content = f.read()
#print(content)
#f.close()
'''
content = f.read(7)
print(content)
content = f.read(3)
print(content)
'''

'''
for printing word by word in line 
for line in content:
    print(line)
'''

'''
for printing sentences in line or in list
f = open("piyush.txt",'r')
for line in f:
    print(line,end='')
'''

'''
print(f.readline())
print(f.readline())

print(f.readlines())#it print lines in list 
'''

'''
#CREATING A FILE
g = open('piyush2.txt','x')
'''

#WRITING AND APPENDING FUNCTIONS
'''
in write mode if we write in a file it will erase all the lines and write new line

we can append on the existing file
'''
'''
#writing
f = open('piyush.txt','w')
f.write('piyush is a sexy boy')
'''
'''
#appending 
f = open('piyush2.txt','a')
f.write('piyush is very handsome boy \n')
a = f.write('piyush is very handsome boy \n')
print(a)
'''
'''
f = open('piyush.txt','a')

while True:
    f.write("piyush is handsome and smart\n")
    
f.close()
'''
'''
#with block
with open('piyush.txt','r') as f:
    a = f.readline()
    print(a)
'''
'''
#for counting lines
def countlines():
    with open('piyush.txt','r') as f:
        r = f.readlines()
        l = len(r)
        print(l)

countlines()
'''
with open('piyush.txt','r') as f:
    
    





