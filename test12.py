import time
start = time.time()
###################################
def triangular_number(num):
    sum=0
    for i in xrange(1,num+1):
        sum+=i
    return sum

def factors(num):
    factor_list=[1]
    for i in xrange(2,num):
        if num%i==0:
            factor_list.append(i)
    else:
        factor_list.append(num)
    return factor_list        

i=0        
while True:
    i+=1
    #print i
    triang=triangular_number(i)
    divisors=factors(triang)
    #print len(divisors)
    if len(divisors)>500:
        break
    
        
print triangular_number(i)    
    






###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 