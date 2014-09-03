import time
start = time.time()
###################################
months=[str(n) for n in range(1,13)]
days_normal=[31,28,31,30,31,30,31,31,30,31,30,31]
days_leap=[31,29,31,30,31,30,31,31,30,31,30,31]
days=('M','T','W','Th','F','Sa','S')

leap_year=dict(zip(months,days_leap))
print leap_year
print months






###################################
elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds") 