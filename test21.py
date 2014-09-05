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
    

#create a list containing all the factor sums till the required number    
# num_list=[]
# sum_list=[]    
# for num in range(2,100):
    # num_list.append(num)
    # sum_list.append(sum_factors(num))
# sumhash=dict(zip(sum_list,num_list))
# numhash=dict(zip(num_list,sum_list))
# print numhash
# amicable_numlist=[]
# for a in numhash:
    # sum_key=numhash[a]
    # if sum_key in numhash:
        # if numhash[sum_key]==a:
            # amicable_numlist.append(a)
            # if sum_key in amicable_numlist:
                # pass
            # else:    
                # amicable_numlist.append(sum_key)
            
        

# for trial in range(1,10000):    
    # if trial in sumhash:
        # if trial=
        # amicable_num = sumhash.get(trial,"None")
        # amicable_numlist.append(amicable_num)
        # if trial in amicable_numlist:
            # pass
        # else:    
            # amicable_numlist.append(trial)
# print len(amicable_numlist)
# print amicable_numlist

# summing the result
# sum=0
# for i in amicable_numlist:
    # sum+=i
# print sum    
###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 