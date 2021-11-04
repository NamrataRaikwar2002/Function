def prime(p):
    i=1
    count=0
    while i<=p:
        if p%i==0:
            count=count+1
        i=i+1
    if count==2:
        return "prime"
    return "not prime"
a=int(input('enter number to check prime or not:'))
print(prime(a))




# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(3))
