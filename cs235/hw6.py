from math import floor
from fractions import gcd
from random import randint



'''
1.
a.
8 * x = 16 (mod 32)

apply the linear congruence theorem,
gcd(8,32) = 8
since 16 belongs to closure({8},+), there is a solution.
    x = 2 (mod 4)

b.

x = 5 (mod 15)
x = 15 (mod 25)

gcd(15,25) = 5

5 = 0 (mod 5)
15 = 0 (mod 5)
So there must be a solution
    x/5 = 1 (mod 3)
    x/5 = 3 (mod 5)
make x/5 = y
    y = 1 (mod 3)
    y = 3 (mod 5)
    y = 13 (mod 15)

so x = 13 *5= 65 (mod 75)

c.

x = 10 (mod 14)
x = 17 (mod 21)

gcd(14,21) = 7

10 = 3 mod 7
17 = 3 mod 7
So there must be a solution
 (x-3)/7 = (10-3)/7 (mod 2)
 (x-3)/7 = (17-3)/7 (mod 3)

 make (x-3)/7 = y, this gives:
 y =  1 (mod 2)
 y =  2 (mod 3)
 y =  5 (mod 6)

 x = 38 (mod 14*21/7)
   = 38 (mod 42)


d.

x^2   = 9 (mod 35)
2 * x = 6 (mod 14)
Solve the first equation:
x^2 = 2 mod 7
x^2 = 4 mod 5

x1 = 3 mod 7
x2 = 4 mod 7

x3 = 2 mod 5
x4 = 3 mod 5



solve the first equation:
applying the different combinations
x1 = 3 (mod 35)
x2 = 32 (mod 35)
x3 = 17 (mod 35)
x4 = 18 (mod 35)

Solve the second equation:
gcd(2,14)= 2
x = 3 (mod 7)

combinations:
x = 3 (mod 35)
x = 3 (mod 7)
x1 = 3

x = 32 (mod 35)
x = 3   (mod 7)
no solution

x = 3 (mod 7)
x = 17 (mod 35)
x2 = 17 (mod 35)

x = 3 (mod 7)
x = 18 (mod 35)
no solution
these two equations have no solution.
As a result the sloution is x1 = 3 mod 35 and x2 = 17 mod 35




e.
x = 6 (mod 12)
x = 4 (mod 16)
gcd(12,16) =  4

6 = 2 (mod 4)
4 = 0 (mod 4)

Because 2 !=  0, as a result, there is no sloution for this question.

f.

{0,1,2,3,4,5,6,7,8,9,10,11}
{0}
{0,4,8}
{0,3,6,9}
{0,2,4,6,8}
{0,2,4,6,8,10}

g.



h.

construct the euqations:
let A  be the total number of problems:
A = 2 mod 12
A=  8 mod 15
Using CRT to solve the equations and because A < 60
So the total number of problems is 38


'''
# Code from previous homework
def egcd(a, b):
    (x, s, y, t) = (0, 1, 1, 0)
    while b != 0:
        k = a // b
        (a, b) = (b, a % b)
        (x, s, y, t) = (s - k*x, x, t - k*y, y)
    return (s, t)      


# Code from previous homework
def inv(a,m):
    if gcd(a,m)!=1 :
        return None
    else:
        (s,t)= egcd(a,m)
    return s%m




# Code from  previous homework
def solveOnePrevious(c,a,m):
    if gcd(c,m)!= 1  :
        return None
    else:
        return (a* inv(c,m))%m


# If it exists, the function should return the unique solution x ∈ ℤ/(m/gcd(c,m))ℤ to the following equation
# c *x	≡a (mod m)
def solveOne(c,a,m):
    n = gcd(c,m)
    if n == 1:
        return solveOnePrevious(c,a,m)
    if a%n!=0:
        return None
    else:
        return solveOnePrevious(c//n,a//n,m//n)


# function solveOneSameMod(c, a, m) that takes three integers c, a, and m ≥ 1. If it exists,
# the function should return the set of all solutions x ∈ ℤ/mℤ to the following equation: c x ≡ a (mod m)
 
def solveOneSameMod(c, a, m):
    x = solveOne(c,a,m)
    if x == None:
        return None
    else:
        return { a for a in range(m) if (a-x)%(m//gcd(c,m))==0}

# Code from homework 3
def solveTwoPrevious(e1,e2):
    if (solveOne(e1[0],e1[1],e1[2]) == None) or (solveOne(e2[0],e2[1],e2[2])==None) or gcd(e1[2],e2[2])!=1 :
        return None
    else:
        x1 = solveOne(e1[0],e1[1],e1[2])
        x2 = solveOne(e2[0],e2[1],e2[2])
        a1 = ((x1*inv(e2[2],e1[2]))%e1[2]*e2[2])%(e1[2]*e2[2])
     
        a2 = ((x2*inv(e1[2],e2[2]))%e2[2]*e1[2])%(e1[2]*e2[2])
        return (a1+a2)%(e1[2]*e2[2])


# solveTwo() should return the unique solution x to the above system of equations.
# If either equation cannot be solved using solveOne(), the function should return None.
def solveTwo(e1,e2):
    if solveOne(e1[0],e1[1],e1[2])==None or solveOne(e2[0],e2[1],e2[2])==None:
        return None
    g = gcd(e1[2],e2[2])
    a = e1[1] % g
    b = e2[1] % g
    if b != a:
        return None
   
    else:
           x = solveTwoPrevious([1,solveOne(e1[0],e1[1],e1[2])//g,e1[2]//g],[1,solveOne(e2[0],e2[1],e2[2])//g,e2[2]//g])
           x = (x*g+a)%(e1[2]*e2[2]//g)
    
    return x
        
# The function should return the unique solution x to the system of equations represented by the list of equations.
# If the system of equations has no solution, the function should return None.
def solveAll(es):
    for i in range(len(es)):
        if solveOne(es[i][0],es[i][1],es[i][2])== None:
            return None
    for i in range(len(es)-1):
        if solveTwo(es[i],es[i+1])==None:
            return None
           
  
        
    if len(es)==1:
        return es[0][1]
  
    else:
        es[1]= (1,solveTwo(es[0],es[1]),es[0][2]*es[1][2])
        return solveAll(es[1:])


# Code given from homework.
def plus256unreliable(x, y):
    r = randint(0,7) - 4
    return (min(255, max(0, ((x + y)%256) + r)))


# plus16(x, y) that reliably returns (x + y) % 16 with 100% accuracy. 
def plus16(x,y):
    return plus256unreliable(plus256unreliable(16*x,16*y),8)//16

# a Python function plus256(x, y) that reliably returns (x + y) % 256 with 100% accuracy.
def plus256(x,y):
    a = plus16(x,y)%3
    b = plus16(x,y)%7
    c = plus16(x,y)%11
    d = plus16(x,y)%13
    return (x+y)%(3*7*11*13)


# Code given from homework
def quantum(a, n):
    return [pow(a,k,n) for k in range(1, n)].index(1) + 1

# function factor(n) that returns a non-trivial factor of a composite number input n = p ⋅ q by calling quantum()
def factor(n):
    a = randint(2,n)
    if gcd(a,n)>1:
        return gcd(a,n)
    r = quantum(a,n)
    while True:
        if r % 2 == 0 and pow(a,r//2,n)!=1:
            break
        else:
            a = randint(2,n)
            if gcd(a,n)>1:
                return gcd(a,n)
            else:
                r = quantum(a,n)
    return  gcd(pow(a,r//2)+1, n)

    
    


    
   
            
    
            
       
        
        
    
    









  
