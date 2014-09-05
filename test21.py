import time
start = time.time()
###################################
def d(num):
    factor_list=[]
    sum=0
    for i in xrange(1,(int(num**0.5)+1)):
        if num%i==0:
            factor_list.append(i)
            if i!=1:
                factor_list.append(num/i)
    for dig in factor_list:
        sum+=dig
    return sum

sum=0
for i in xrange(1,10000):
    x=d(i)
    y=d(x)
    if i==y and i!=x:
        sum+=i
print sum        
###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 