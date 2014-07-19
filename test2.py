sum=0
ft=1
st=2
    
while st < 4000000:
    if st%2==0:
        sum+=st
    next_term = ft+st
    #print next_term
    ft=st
    st=next_term
    
    
print sum        