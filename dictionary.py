# DICTIONARY
'''
python dictionary In-built functions are -
len(), any(), all(), sorted()

python dictionary In-built methods are -
keys(), value(), items(), get(), clear(), copy(), pop(), popitems(), fromkeys(), update()
'''

a = {1:'piyush',5:'bachcha',3:'swet',4:'sorav'}
b = {'':2,0:3}
print(len(a))
print(any(b))#it will return false if all key is none or 0. There should be atleast one key which is appropriate
print(all(a))#it will return TRUE if all keys are existed 
print(sorted(a))#it will display the sorted keys of the dictioanry in the form list[]


print(a.keys())
#dict_keys([1,5,3,4])
print(a.values())
#dict_values(['piyush','bachcha','swet','sorav'])
print(a.items())
#dict_items([(1,'piyush'),(5,'bachcha'),(3,'swet'),(4,'sorav')])

print(a.get(3))#in this 3 is key 
#swet
print(a.get(6))
#None
print(a.get(6,14))#there is no key names 6, therefore it will return 14 
#14

#a.clear()#it will clear all the items in a dictionary including all the keys and values

c = a.copy()
print(c)
#{1: 'piyush', 5: 'bachcha', 3: 'swet', 4: 'sorav'}

print(a.pop(3))#in this is a key
#swet #this is removed from dictionary 
#print(a.pop(6))
#KeyError
print(a.pop(6,9))
#9

print(a.popitem())#it will remove the last item of the dictionary
#(4, 'sorav') # this is removed from a dictioanry 


L = []
B = {}
print(B.fromkeys(L))
#{'NAME': None, 'CLASS': None, 'ROLLNO': None, 'SECTION': None}
#OR
class10={}
class10 = B.fromkeys(L,10)#all values of dictionary will be 10
print(class10)
#{'NAME': 10, 'CLASS': 10, 'ROLLNO': 10, 'SECTION': 10}

u = {'NAME':'PIYUSH','CLASS':10,'ROLLNO':22334869,'SECTION':'B'}
u.update({'ADDRESS':'CHANDIGARH'})
print(u)
#{'NAME': 'PIYUSH', 'CLASS': 10, 'ROLLNO': 22334869, 'SECTION': 'B', 'ADDRESS': 'CHANDIGARH'}
k = {'NAME':'SWET','SUB':'MATHS','MARKS':69}
u.update(k)
print(u)
#{'NAME': 'SWET', 'CLASS': 10, 'ROLLNO': 22334869, 'SECTION': 'B', 'ADDRESS': 'CHANDIGARH', 'SUB': 'MATHS', 'MARKS': 69}
#it avoid duplicate values and keys and return changed values


