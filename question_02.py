z=input('enter world:').strip()
a=''
for i in z:
    if i not in a:
        a+=i
        
print(a)