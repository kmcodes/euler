import time
start = time.time()
def is_prime(num):
    for i in range(2,int(num**.5+1)):
        if num%i==0:
            return False
            break
        else:
            i+=1
    return True

num, i = 1, 0
sum=2
while num<2000000:
    num+=2
    if is_prime(num):
        #print num
        sum+=num
print sum
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 