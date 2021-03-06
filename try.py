import time
start = time.time()
###################################
def isprime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 
print isprime(999983) 

###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 