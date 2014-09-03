import time
start = time.time()
def eratosthenes2(n):
    sum=0
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            
            sum+=i
            multiples.update(range(i*i, n+1, i))
    return sum
 
print eratosthenes2(2000000)
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 
