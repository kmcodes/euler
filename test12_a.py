def factors_len(num):
    factor_list=[1]
    for i in xrange(2,(int(num*0.5)+1)):
        if num%i==0:
            factor_list.append(i)
    else:
        factor_list.append(num)
    return factor_list
fact=factors_len(input())    
print len(fact)
print fact