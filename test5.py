def div_test(num,pflist):
    for i in pflist:
        if num%i==0:
            if i>=20:
                return True
                break
            else:
                i+=1
        else:
            return False
            break

''' work on this and use the LCM method to calculate
def factor:
    
    pass
def is_prime:
    pass
   '''      
            
num=232792550
pflist=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

while num > 232792470:
    if div_test(num,pflist):
        break
    else:
        num+=1
        
print num        
        