#LIST

l = [23,3,4,6,7,9,9]
print(len(l))
print(l.index(9))
print(l.count(9))

l.append(69)
print(l)
b=[12,45]
l.append(b)
print(l)
#[23, 3, 4, 6, 7, 9, 9, 69, [12, 45]]

l.extend([56,78])
print(l)
#[23, 3, 4, 6, 7, 9, 9, 69, [12, 45], 56, 78]

l.pop(8)
print(l)

l.insert(0,1)
print(l)
#[1, 23, 3, 4, 6, 7, 9, 9, 69, 56, 78]


