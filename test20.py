import time
start = time.time()
###################################
def fact(n):
    fact_num=1
    for num in range(n,1,-1):
        fact_num*=num
    return fact_num
        
def dig_sum(num):
    d_s=0
    for dig in str(num):
        d_s+=int(dig)
    return d_s
      
print dig_sum(fact(100))




###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 