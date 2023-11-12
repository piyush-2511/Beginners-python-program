'''
#ERROR HANDLING
a = input("Enter the number : ")
print(f"Multiplication of {a} : ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

print('some imp codes of lines ')
print('end of Program ')
'''
'''
OUTPUT
Enter the number : piyush
Multiplication of piyush : 
invalid literal for int() with base 10: 'piyush'
some imp codes of lines 
end of Program
'''
'''

#VlaueError , IndexError

try:
    num = int(input('Enter the number : '))
    a = [6,9]
    print(a[num])
except ValueError:
    print('Number entered is not an integer ')
except IndexError:
    print('Index Error')
  
#FINALLY

def func():
    try:
        l = [1,2,3,4]
        i = int(input('Enter the index : '))
        print(l[i])
        return 1
    except:
        print('Some error occured')
        return 0
    print('I am always executed')
   #in this print will not display in the output because the cursor will return from return keyword

    
def func():
    try:
        l = [1,2,3,4]
        i = int(input('Enter the index : '))
        print(l[i])
        return 1
    except:
        print('Some error occured')
        return 0
    finally:
        print('I am always executed')#Because of FINALLY CLAUSE it will print anyhow

func()


'''

#CUSTOM ERRORS

a = int(input('Enter the number between 5 and 9 : '))
try:
    if a<5 or a>9:
        raise ValueError('Value should be between 5 and 9')
    except ValueError:
        elif a == 'quit':
    




