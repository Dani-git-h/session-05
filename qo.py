z = input('enter word:')
d = z.split()
most0 = d[0]
max1 = 0 
for i in d:
    n=0
    for j in d:
        if i==j:
            n+=1
    if n >max1:
        max1=n
        most0=i
print(most0,'->',max1)