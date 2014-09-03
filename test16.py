import time
start = time.time()
###################################

power=2**1000
sum=0
for dig in str(power):
    print dig
    sum+=int(dig)
print sum    

###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 