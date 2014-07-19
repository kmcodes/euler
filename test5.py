def div_test(num):
    for i in range(2,21):
        if num%i==0:
            if i>=20:
                 return True
                break
            else:
                i+=1
        else:
            return False
            break
            
num=232792550

while num > 232792470:
    if div_test(num):
        break
    else:
        num+=1
        
print num        
        