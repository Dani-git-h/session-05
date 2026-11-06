#01
p=input('enter password:')
error=0
if len(p)<=8:
    print('password must be at least 8 characters long.')
    error+=1
if not any(i.isupper() for i in p):
    print('password must contain at least one uppercase letter.')
    error+=1
if not any(i.islower() for i in p):
    print('password must contain at least one lowercase letter.')
    error+=1
if not any (i.isdigit()for i in p):
    print('password must contain at least one number.')
    error+=1
if not any(i in '!@#$%^&*'for i in p):
    print('password must contain at least one special character.')
    error+=1
if error>0:
    print('password rejected')
else:
    print('password accepted.')
    
    
    