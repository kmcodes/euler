import time
start = time.time()
###################################
def fibonacci():
    current = 0 
    previous = 1
    while True:
        temp = current
        current = current + previous
        previous = temp
        yield current


for index, element in enumerate(fibonacci()):
    if len(str(element)) >= 1000:
        answer = index + 1 #starts from 0
        break
print(answer)

###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 
