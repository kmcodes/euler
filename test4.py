def digit_count(n):
    i=0
    while n!=0:
        n=n/10
        i+=1
    return i
def is_palindrome(n):
    digits_list=[]
    num=n
    rev=0
    count=digit_count(n)
    for i in range(count):
        digits_list.append(n%10)
        n/=10
    rev_list=digits_list[::-1]    
    for i in range(count):
        rev=rev+(rev_list[i]*(10**i))
    if num==rev:
        return True
    else:
        return False
largest=0
for i in range(100,999):
    for j in range(100,999):
        number=i*j
        if is_palindrome(number):
            if number>largest:
                largest=number
print largest                
                
    
