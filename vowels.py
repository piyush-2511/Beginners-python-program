vowels = ['a','e','i','o','u']
st = input('ENTER STRING : ')
stt = st.lower()
v = 0
c = 0
for x in stt:
    if x in vowels:
        v += 1
    else:
        c+=1
print('vowels:',v)
print('constant:',c)
