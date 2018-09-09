from math import floor
from fractions import gcd

# Lai Wei
# laiw12@bu.edu
'''
a.

5 * x = 3 (mod 7)
    x = 3 * 5^(-1)

Apply Fermat's little theorem
    x = 3 * 5^(7-2)
    x = 3 * (4*4*5)
    x = 3 * 3
    x = 2 (mod 7)
    

b.

4 * x = 2 (mod 11)
    x = 2 * 4^(-1)

Apply Fermat's little theorem
    x = 2 * 4^(11-2)
    x = 2 * 4^(9)
    x = 2 * (5*5*5*5*4)
    x = 2 * (3*3*4)
    x = 2 * 3
    x = 6 (mod 11)

c.
x = 3 (mod 7)
x = 1 (mod 5)

x1 = 3 (mod 7)
x1 = 0 (mod 5)
x2 = 1 (mod 5)
x2 = 0 (mod 7)

solve for x1:
x1 = 5 * y1  because x1 is a multiple of 5
5 * y1 = 3 (mod 7)
    y1 = 3 * 5^(-1)
    y1 = 3 * 5^(7-2)
    y1 = 3 * 5^(5)
    y1 = 3* (4*4*5)
    y1 = 2
x1 = 10 (mod 35)

solve for x2:
x2 = 7 * y2 because x2 is a multiple of 7
7 * y2 = 1 (mod 5)
    y2 = 1 * 7^(3)
    y2 = 1 * (2*2*2)
    y2 = 3
x2 = 21 (mod 35)

Thus the solution to the orginal system is:
x1+x2 =  31 (mod 35)
x = 31 + 35Z

d.
x = 2 (mod p)
x = 4 (mod q)
slove for x1:
x1 = 2 * q * q^(-1)  mod( p*q)
x1 = 6* q (mod p*q)

slove for x2:
x2 = 4 * p * p(-1) mod(p*q)
x2 = 20*p (mod p*q)

Thus the sloution to the orginal system is:
x = x1+x2 = 6q + 20p (mod p*q)



e.
Applying the formula:
x = 3 (mod 4)
x = 6 (mod 9)

9^(-1) =  1 (mod 4)
4^(-1) =  4 (mod 9)

x1 = 3*9*1 (mod 36)
   = 27
   
x2 = 6*4*1 (mod 36)
   = 24



Thus the sloution to the orginal system is:
x = x1 + x2 = 51 ( mod 36)
x = 15 (mod 36)

f.

2 * x = 1 (mod 5)
x = 10 (mod 14)

simplify the first equation:
x = 1* 2^(5-2)
x = 3 (mod 5)

now we have:
x = 3 (mod 5)
x = 10 (mod 14)

solve for x1:
x1= 3 ( mod 5)
x1= 0 ( mod 14)

14y1 = 3 (mod 5)
  y1 = 3^14(3)
  y1 = 2 (mod 5)
  x1 = 28 mod(70)

solve for x2:

x2 = 10 (mod 14)
x2= 0  (mod 5)

5y2 = 10 (mod 14)
 y2 = 10*5^(-1)

first compute φ(14) = 2*7 = 1*6 = 6

5^(-1) = 5^(φ(14)-1) (mod 14)
       = 5^5
       = 3
   y2 = 10*3 (mod 14)
      = 2
   x2 = 10 mod(70)

The general solution is :
x1+x2 = x = 38 (mod 70)
   





'''


#a function invPrime(a, p) that takes two integers a and p > 1 where p is prime.
#The function should return the multiplicative inverse of a ∈ ℤ/pℤ (if a ≡ 0, it should return None).
def invPrime(a,p) :
    if a == 0:
        return None
    else:
        return pow(a,p-2,p)


# from the professor 
def egcd(a, b):
    (x, s, y, t) = (0, 1, 1, 0)
    while b != 0:
        k = a // b
        (a, b) = (b, a % b)
        (x, s, y, t) = (s - k*x, x, t - k*y, y)
    return (s, t)


#a function inv(a, m) that takes two integers a and m > 1. If a and m are coprime, it should return the multiplicative inverse of a ∈ ℤ/mℤ.
#If a and m are not coprime, it should return None.
def inv(a,m):
    if gcd(a,m)!=1 :
        return None
    else:
        (s,t)= egcd(a,m)
    return s%m
           


# n solveOne(c, a, m) that takes three integers c, a, and m ≥ 1. If c and m are coprime, the function should return the solution x ∈ {0, ..., m-1}
def solveOne(c,a,m):
   
        return (a* inv(c,m))%m


# a function solveTwo(e1, e2) that takes two tuples e1 and e2 as inputs, each of the form (c, a, m) (i.e., containing three integer elements).
def solveTwo(e1,e2):
 
        x1 = solveOne(e1[0],e1[1],e1[2])
        x2 = solveOne(e2[0],e2[1],e2[2])
        a1 = ((x1*inv(e2[2],e1[2]))%e1[2]*e2[2])%(e1[2]*e2[2])
     
        a2 = ((x2*inv(e1[2],e2[2]))%e2[2]*e1[2])%(e1[2]*e2[2])
        return (a1+a2)%(e1[2]*e2[2])


# solveAll(es) that takes a list of one or more equations, each of the form (c, a, m)
def solveAll(es):
    for i in range(len(es)):
        if solveOne(es[i][0],es[i][1],es[i][2])== None:
            return None
           
  
        
    if len(es)==1:
        return es[0][1]
  
    else:
        es[1]= (1,solveTwo(es[0],es[1]),es[0][2]*es[1][2])
        return solveAll(es[1:])


#that takes a list of one or more tuples nes (i.e., nes is of the form [(a1,n1),...,(ak,nk)]) as its first argument,
#and a list of one or more primes ps (i.e., of the form [p1,...,pm]) as its second argument.
#The function should return the correct result of the sum of powers as long as the following is true (e.g., on a computer with unlimited memory and time):
#0   ≤   a1n1 + ... + aknk <   p1 ⋅ ... ⋅ pm
def sumOfPowers(nes,ps):
    c=0
    a=1
    b=[0]*len(nes)
    for i in range(len(ps)):
        a = a * ps[i]
    
    for j in range(len(nes)):
        if nes[j][0]<0 and nes[j][1]%2!=0:
           
            b[j]=pow(nes[j][0],nes[j][1],a)-a
        else:
            b[j] = pow(nes[j][0],nes[j][1],a)
    for x in range(len(b)):
        c=c+b[x];
    return c
        
        
        

    
        
                   
  

    





    
    
