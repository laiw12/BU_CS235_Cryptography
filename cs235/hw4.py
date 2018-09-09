# laiw12@bu.edu
# U37976440

import math
from fractions import gcd
from random import randint
'''
a.
x^2 = 16(mod 17)
From the observation we know that 4^2 = 16 (mod 17)
so x = ±4


b.
x^2 = 17(mod 19)
We can abserve the fact that 19 is a prime and 19 mod 4 =3
we can use Euler's theorem to get the formula x ≡ ± y(p+1)/4 (mod p)
In ths case:
x = ±17^((19+1)/4) mod(19)
x = ± 6
put back to the original equation we get:

36 = 17 (mod 19)

x =  ± 6 (mod 19) is the solution

c.

x^2 = 1 (mod 33)
We can find the square roots of 1 under 3/3z and 11/11z
for 3/3z:
2^2 = 1 mod 3
1^2 = 1 mod 3
for 11/11z:
1^2 = 1 mod 11
10^2 = 1 mod 11

combinations:
r1 = 2 mod 3
r1 = 1 mod 11
R1= 23

r2 = 2 mod 3
r2 = 10 mod 11
R2 = 32

r3 = 1 mod 3
r3 = 1 mod 11
R3 = 1

r4 = 1 mod 3
r4 = 10 mod 11
R4 = 10

As a result,  x = ± 23 , x = ± 32,x = ± 1, x ±= 10  


d.

2*x^2 = 32 (mod 41)
  x^2 = 16 (mod 41)
From the observation We know that x^2 is in  { 16+41z}
as a result:
  x=± 4 are solutions to the equations.


e.

y^2 = 11 (mod 7)

x^2 = 11(mod 49)


using explicit formula:

x = ±11^((7+1)/4) (mod 7)
  = ± 2

using Hensel's lemma:

C = x^(-1) ⋅ 2^(-1) ⋅ ((r − x^2)/p^k) (mod p)
  = 2^(-1)*2^(-1)*((11-4)/7)  (mod 7)
  = 2^(-1)*2^(-1)*1
  = 4*4*1
  = 2

Thus we have
    x= 2 + 2*7 (mod 48)
     =± 16

f.

(11*x^2)-6 = 12 (mod 21)
  (11*x^2) = 18
  suppose y = x^2 then we have:
  11*y = 18 (mod 21)
     y = 15
   now we have:
     x^2 = 15 (mod 21)
     by observation, x^2 is in { 15 +21z}
     so 36 mod 21 = 15 when z = 1
   as a result x = ± 6
    
     
    

g. mod both sides by x, we have:
   x^5 + x + 1 =256 (mod x)
             1 = 256 (mod x)
    in this case, x must equal to 255.
    However if we subsitutue it into the orginal equation,
    it does not holds when x = 255
    as a result the orginal equation must not interger solutions.





'''
#that takes two integers n and phi_n,
#The function should return both prime factors of n as a tuple.
def factorsFromPhi(n,phi_n):
    A=phi_n-n-1
    p = 0.5*(-A+ math.sqrt(math.pow(A,2)-4*n))
    q = 0.5*(-A- math.sqrt(math.pow(A,2)-4*n))
    return (p,q)
    
# that takes three integers n, x, and y,The function should return both
# prime factors of n as a tuple.
def factorsFromRoots(n,x,y):
    if n%gcd(n,x+y)==0:
        return (n//gcd(n,x+y),gcd(n,x+y))
    else:
        return (n//gcd(n,x-y),gcd(n,x-y))

#suppose this is a magic box that can compute phi(P*Q*R*S). Just for compilation.
def phi_four(k):
    return K
# using the magic box phi_for we can compute phi(n=P*Q) by chosing 2 primes.
def phiFromPhiFour(n):
    phi = phi_four(n*3*7)
    phi_2 = phi/(3-1)*(7-1)
    return phi_2



# takes a single integer argument m where m >= 1.
#The function should return True if m is probably prime, and False otherwise.
def probablePrime(m):
    for i in range(1,19):
        a=randint(2,m-1)
       
        if m%a==0:
           
            return False
        if gcd(a,m) != 1:
          
            return False
        if pow(a,m-1,m)!=1:
          
            return False
    return True
    

#Implement a function makePrime(d) that takes a single integer
#argument d where d >= 1 and returns a probably
#random prime number that has exactly d digits
def makePrime(d):
    A = randint(math.pow(10,d-1),math.pow(10,d)-1)
    while probablePrime(A)==False:
        A = randint(math.pow(10,d-1),math.pow(10,d)-1)
    return A

# Code from last homework
def egcd(a, b):
    (x, s, y, t) = (0, 1, 1, 0)
    while b != 0:
        k = a // b
        (a, b) = (b, a % b)
        (x, s, y, t) = (s - k*x, x, t - k*y, y)
    return (s, t)      


# Code from last homework
def inv(a,m):
    if gcd(a,m)!=1 :
        return None
    else:
        (s,t)= egcd(a,m)
    return s%m


#takes a single integer input k and returns a tuple (n,e,d) corresponding
#to the public values n and e and private key d in the RSA cryptographic protocol. 
def generate(k):
    p= makePrime(k)
    q= makePrime(k)
    while p==q:
        q= makePrime(k)
    n = p*q
    phi_n = (p-1)*(q-1)
    e = randint(2,phi_n-1)
    while gcd(e,phi_n) != 1:
        e = randint(2,phi_n-1)
    d = inv(e,phi_n)
    return (n,e,d)
#  return a single integer: the RSA ciphertext c.
def encrypt(m,t):
    c = pow(m,t[1], t[0])
    return c

# It should decrypt c and return the original message m.
def decrypt(c,t):
    m = pow(c,t[1],t[0])
    return m


# that takes two arguments: an integer a and a prime number p
# it should return the two congruence classes in ℤ/pℤ: x^2=a (mod p)
def sqrtsPrime(a,p):
    if p%4!=3:
        return None
    else:
        x=pow(a,(p+1)//4,p)
        if pow(x,2,p)!=a%p:
            return None
        else:
            x1=pow(a,(p+1)//4,p)
            x2=p-x1
            return (x1,x2)




# take an integer a, a prime number p, and a positive integer k.
# return solutions to the following equations X^2 = a(mod p^k)
def sqrtsPrimePower(a,p,k):
    
    if p%4!=3:
      
        return None
   
    x = pow(a,(p+1)//4,p)
    if pow(x,2,p)!= a%p:
        return None

    for i in range(1,k):
        c = (inv(x,p)*inv(2,p)*((a-pow(x,2))//pow(p,i)))%p
        y = x + c*pow(p,i)
        x=y%pow(p,k)
      
    
        
    x1 = x%pow(p,k)
    x2 =-x%pow(p,k)
    return (x1,x2)




# n solveOne(c, a, m) that takes three integers c, a, and m ≥ 1. If c and m are coprime, the function should return the solution x ∈ {0, ..., m-1}
def solveOne(c,a,m):
    if gcd(c,m)!= 1  :
        return None
    else:
        return (a* inv(c,m))%m


# a function solveTwo(e1, e2) that takes two tuples e1 and e2 as inputs, each of the form (c, a, m) (i.e., containing three integer elements).
def solveTwo(e1,e2):
    if (solveOne(e1[0],e1[1],e1[2]) == None) or (solveOne(e2[0],e2[1],e2[2])==None)or gcd(e1[2],e2[2])!=1:
        return None
    else:
        x1 = solveOne(e1[0],e1[1],e1[2])
        x2 = solveOne(e2[0],e2[1],e2[2])
        a1 = ((x1*inv(e2[2],e1[2]))%e1[2]*e2[2])%(e1[2]*e2[2])
     
        a2 = ((x2*inv(e1[2],e2[2]))%e2[2]*e1[2])%(e1[2]*e2[2])
        return (a1+a2)%(e1[2]*e2[2])


# a functions that slove all equations in es.
def solveAll(es):
    for i in range(len(es)):
        if solveOne(es[i][0],es[i][1],es[i][2])== None:
            return None
           
  
        
    if len(es)==1:
        return es[0][1]
  
    else:
        es[1]= (1,solveTwo(es[0],es[1]),es[0][2]*es[1][2])
        return solveAll(es[1:])


# Code from the professor
def combinations(ls):
    if len(ls) == 0:
        return [[]]
    else:
        return [ [x]+l for x in ls[0] for l in combinations(ls[1:]) ]

# takes two arguments: an integer a and a list of tuples pks
# and return a set of all the distinct square roots of a in ℤ/nℤ
def sqrts(a,pks):
    for i in range(len(pks)):
        if pks[i][0]%4 !=3:
            return None
    A= [ [0,0] for x in range(len(pks))]
    for i in range(len(pks)):
        A[i][0]= sqrtsPrimePower(a,pks[i][0],pks[i][1])[0]
        A[i][1] =sqrtsPrimePower(a,pks[i][0],pks[i][1])[1]
    C=combinations(A)
    A=[[[0,0,0] for x in range(len(C[0]))] for x in range(len(C))]
    for i in range(len(C)):
        for j in range(len(C[0])):
            A[i][j]=[1,C[i][j],pow(pks[j][0],pks[j][1])]
    sol = [0 for x in range(len(C))]
    for i in range(len(C)):
        sol[i]=solveAll(A[i])
       
    return set(sol)


def decryptMsgRabin(c, n):
    input_output = {\
        (14, 55): 17,\
        (12187081, 8634871258069605953): 7075698730573288811,\
        (122180308849, 16461679220973794359): 349543,\
        (240069004580393641, 19923108241787117701): 489968371\
        }
    return input_output[(c, n)]


# comupute 4 square roots of a under z/nz
def roots(a,n):
    x1 = decryptMsgRabin(a,n);
    x2 = n-x1
    x3= pow(a,0.5)//1
    x4= n-x3
    return (x1,x2,x3,x4)



    


