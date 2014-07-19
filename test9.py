#Timer Function to find execution time

import timeit
start = timeit.default_timer()

#end timer init

#Identify if pythagorean tiplet
def pyth(a,b,c):
    if c**2 == a**2 + b**2:
        return True
    else:
        return False
#actual program clear        
prod=0        
for a in range(1,998):
    for b in range (1,998):
        c=1000-b-a
        if pyth(a,b,c):
            print a,b,c
            prod=a*b*c
            break
    else:
        continue
    break  
print prod    

#End timer and print time
stop = timeit.default_timer()
print stop - start 