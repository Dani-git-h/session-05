z=input('enter word:')
r=""
x=1
if not z:
    print("")
else:
    for i in range(1,len(z)):
        if z[i] == z[i-1]:
            x += 1
        else:
            r += z[i-1] + str(x)
            x=1
    r += z[-1] + str(x)
    print(r)