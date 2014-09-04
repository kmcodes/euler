import time
start = time.time()
###################################
def triangular_number(num):
    sum=0
    for i in xrange(1,num+1):
        sum+=i 

    return sum

def factors_len(num):
    factor_list=[]
    for i in xrange(1,(int(num**0.5)+1)):
        if num%i==0:
            factor_list.append(i)
            factor_list.append(num/i)
    
    return len(factor_list)

i=1
max=0 

while True:
    i+=1
    #print i
    triang=triangular_number(i)
    if factors_len(triang)> max:
        max = factors_len(triang)
        print max
    if max>500:
        break
        
print triang 
###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 