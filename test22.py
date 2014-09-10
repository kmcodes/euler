import time
start = time.time()
###################################
def score(name):
    sum=0
    for alphabet in name:
        num=ord(alphabet)-64
        sum+=num
    return sum    

f=open("text22.txt",'r')
names=f.read().split(',')
f.close
names.sort()

sum=0
for i,x in enumerate(names,1):
    scores=[]
    x=x[1:-1]
    sum+=(score(x)*i)
    
print sum    
###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")
