import time
start = time.time()
###################################
count=0
n_count=0
flag=0
n=0

def iseven(x):
    if x%2==0:
        return True
    else:
        return False
for start_num in range(1,1000000):
    n=start_num+1
    while n!=1:
        if iseven(n):
            n=n/2
        else:
            n=3*n+1
        n_count+=1
    if n_count>count:
        count=n_count
        n_count=0
        flag=start_num+1
    else:
        n_count=0
print flag        
        

    






###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 