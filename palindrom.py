st = input("ENTER ANY NAME : ")
l = len(st)
mid = l/2
rev = -1
for a in (st):
    if st[a]==st[rev]:
        a += 1
        rev -= 1
        print("it is a palindrom")
    else:
        print("it is not a palindrom")
        

        
