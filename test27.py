import time
start = time.time()
###################################
def isprime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True 

def n_value(a,b):
    value=0
    n=0
    while True:
        value=((n*n)+(a*n)+b)
        if isprime(value):
            n+=1
        else:
            break
    return n-1        
large_n=0
large_a=0
large_b=0
for a in xrange(-999,1000,1):
    for b in xrange(-999,1000,1):
        current_n= n_value(a,b)
        if current_n>large_n:
            large_n=current_n
            large_a=a
            large_b=b
print large_a*large_b            
###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 