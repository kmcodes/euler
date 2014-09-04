import time
start = time.time()
###################################
list_1=[i for i in range(10,-1,-1)]

for index, i in enumerate(list_1):
    print list_1[index-1]
###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 
