def sum_factors(num):
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

#create a list containing all the factor sums till the required number    
num_list=[]
sum_list=[]    
for num in range(1,1000):
    num_list.append(num)
    sum_list.append(sum_factors(num))
sumhash=dict(zip(sum_list,num_list))

for trial in range(1,1000):
    amicable_numlist=[]
    if trial in sumhash:
        amicable_num = sumhash.get(trial,"None")
        if trial in amicable_numlist:
            pass
        else:    
            amicable_numlist.append(amicable_num)
            amicable_numlist.append(trial)
print amicable_numlist            