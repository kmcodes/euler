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
    
    
###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 
