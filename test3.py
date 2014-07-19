def isprime(n):
    flag= True
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            flag=False
            break
        else:
            i+=1
            flag = True
    return flag
    
def isfactor(num,den):
    if num%den==0:
        factor=True
    else:
        factor=False
    return factor    
    
num=600851475143

for i in range(2,(int(num**.5)+1)):
    if isfactor(num,i):
        if isprime(i):
            largest_factor=i
            i+=1
        else:
            i+=1
print largest_factor