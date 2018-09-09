# name: Lai Wei
# Email: laiw12@bu.edu
 
'''
 a.  2*x + 1 = 1 (mod 3)
         2*x = 0 (mod 3)
           x = 0 (mod 3)
           x = 0 + 3z

 b.  5*x + 3 = 6 (mod 11)
         5*x = 3 (mod 11)
         5*x = 25 (mod 11)
           x =5 (mod 11)
           x= 5 +11z

 c.  5 + 2*x = 8 (mod 10)
         2*x = 3 (mod 10)
         list the set { 3,13,23,33,...}
         So there is no solution 


 d.     12*x = 3 (mod 4)
        becase 12 = 0 (mod 4) we can replace 12
         0*x = 3 (mod 4)
           0 = 3 (mod 4)
        So there is no possible congruence class that will make the formula true

  e.    9*x = 81 (mod 587)
        since 9 and 587 are coprime
          x = 9 (mod 587)
          x = 9 + 587z
        
  f.    10*x - 3 = 3 (mod 5)
            10*x = 6 (mod 5)
            becase 10 = 0 (mod 5) so we can replace 10
             0*x = 6 (mod 5)
               0 = 6 (mod 5)
        So there is no possible congruence class that will make the formula true

   g.   13*x + 19 = 188 (mod 401)
             13*x = 169 (mod 401)
             since 13 and 401 are coprime
                x = 13  (mod 401)
                x = 13 + 401z

   h.   324637* x = 65109355834657447 (mod 1111111111111111111)
                since 324637 and 1111111111111111111 are coprime
                x = 200560490131 ( mod 1111111111111111111)
                x = 200560490131 + 1111111111111111111z

   i.  2213718098378353198*x ≡ 1 (mod 65109355834657447)
          since   2213718098378353198*x = 0 (mod 65109355834657447)
                         0*x = 1 (mod 65109355834657447)
        So there is no possible congruence class that will make the formula true
'''
from fractions import gcd
from math import log


#  takes two arguments: a target integer t and a list of integers ks. The function
#  should return the integer k in ks that is closest to t
def closest(t,ks):
    var = 0
    var1 =  abs(t-ks[0])
    for i in range(1,len(ks)):
        if abs(t- ks[i])< var1:
            var = ks[i]
            var1 =abs(t- ks[i])

    return var

#function findCoprime(m) that takes a single positive integer argument m and returns an
#integer b where b > 1 and b is coprime with m
def findCoprime(m):
    if m<=3:
        return 3
    if m<=100:
        x=[ a for a in range(3,m)]
        p = closest(m,x)
    else:
        p = (3*m)//7
    while gcd(p-1,m) != 1:
        p = p*gcd(p-1,m)
    return p-1



#takes two positive integer arguments: m represents the upper bound of random numbers to be generated,
#and i represents an index specifying which random number in a the sequence should be generated.
def randByIndex(m, i):
    b = findCoprime(m)
    return (b*i)%m


# takes a single integer argument m where m >= 1. The function should return True if m is probably prime,
# and False otherwise.
def probablePrime(m):
    for k in range(3,10):
        a=randByIndex(m,k)
        while a<2:
            k=k+1
            a=randByIndex(m,k)
       
        if m%a==0:
            return False
        if gcd(a,m) != 1:
            return False
        if pow(a,m-1,m)!=1:
            return False
    return True
    
# Implement a function makePrime(d) that takes a single integer argument d where d >= 1 and returns a probably
# prime number that has exactly d digits
def makePrime(d):
    A = [randByIndex(pow(10,d)-pow(10,d-1),i) for i in range(8000)]
    for i in range(len(A)):
        A[i] = A [i] + pow(10,d-1);
        if probablePrime(A[i]):
            return A[i]
    
    
         
    
     
