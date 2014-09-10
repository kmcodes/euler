import time
start = time.time()
###################################
def digits(num):
    digits=str(num)
    dig_list=[int(dig) for dig in digits]
    return dig_list
def remake(digits):
    num = int(''.join(map(str,digits)))
    return num
def isprime(n):
    flag= True
    if n%2==0 and n>2:
        return False
    else:
        for i in range(2,int(n**.5)+1):
            if n%i==0:
                return False
                break
            else:
                i+=1
                flag = True
        return flag
def replace_digits(num,i):
    d_list=digits(num)
    for d in d_list:
        
    

    
###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 
