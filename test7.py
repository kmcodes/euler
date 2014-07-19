def is_prime(num):
    for i in range(2,int(num**.5+1)):
        if num%i==0:
            return False
            break
        else:
            i+=1
    return True
    
num, i = 1, 0

while i<10001:
    num+=1
    if is_prime(num):
        i+=1
print num