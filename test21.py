def factors(num):
    factor_list=[]
    sum=0
    for i in xrange(1,(int(num**0.5)+1)):
        if num%i==0:
            factor_list.append(i)
            if i!=1:
                factor_list.append(num/i)
    for dig in factor_list:
        sum+=dig
    return factor_list
def sum_list(factor_list):
    for dig in factor_list:
        sum+=dig
    return sum    
    
print sum(factors(220))