file=open('test_13.txt','r')
num_list=[int(line) for line in file]
b=str(sum(num_list))
print b[:10]

