s = {2,3,4,5}
s2 = {5,2,8,9,0}

empset = set()
print(type(empset))

print(s.union(s2))#in union SAME values are not printed

s.update(s2)
print(s)

empset = s.union(s2)#it will UPDATE the new set 
print(empset)

cities = {'tokyo','madrid','berlin','delhi'}
cities2 = {'tokyo','seoul','kabul','madrid'}
cities3 = set()
print(cities.intersection(cities2))#it will return the SAME values of two sets

#cities.intersection_update(cities2)
#print(cities)#it will write the SAME values of both the sets and remove all other values

cities3 = cities.symmetric_difference(cities2)#it will return the NON SAME values of two sets 
print(cities3)
#{'kabul', 'delhi', 'berlin', 'seoul'}

print(cities)
print(cities2)
print(cities3)
print(cities.difference(cities2))# it will compare cities with cities2 and return the DIFFERENT(NON SAME) values
#{'berlin','delhi'}
print(cities2.difference(cities))
#{'kabul', 'seoul'}

print(cities.isdisjoint(cities2))# it will return False if any value are same in two sets
#False

print(cities.issuperset(cities2))# it will return FALSE if cities2 is not a SUBSET of cities
#False

print(
