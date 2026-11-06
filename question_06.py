z = input('enter word: ')
l = z.split()
word = ['hack','froud','scam','password','atack']
for i in word:
    n=0
    for d in l:
        if i==d:
            n+=1
    if n>0:
        print(i,'->',n)