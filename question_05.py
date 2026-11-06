#05
z = input('enter text : ')
a = z.split()
long =a[0]
for i in a :
    if len(i)>len(long):
        long = i
print(long,len(long))