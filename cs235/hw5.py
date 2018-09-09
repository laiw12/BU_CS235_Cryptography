## Lai Wei
## laiw12@bu.edu

from math import floor
from fractions import gcd
from random import randint
from urllib.request import urlopen




'''
1.a

[3,4,5,0,2,1] o [5,4,3,1,0,2] = [1,0,2,5,3,4]

b.

[701,702,...,999,0,1,2,3,4,...,700] o [101,102,...,999,0,1,2,3,4,...,100]
= [702,703,....,999,0,1,...,100,101,102,....,701]

c.

p o p o p o p o [6,0,1,2,3,4,5] = [0,1,2,3,4,5,6] o [6,0,1,2,3,4,5]
                                = [6,0,1,2,3,4,5]
d.
Pick 
     p = [2,3,4,5,6,7,0,1] p^(-1)= [1,0,7,6,5,4,3,2]
     q = [1,2,3,4,5,6,7,0] q^(-1)= [0,7,6,5,4,3,2,1]

  p o q o p-1 o q-1 =[2,3,4,5,6,7,0,1]

e.

[0,1]    1+6z
[1,0]    1+5z

table:
S2                            
[0,1] o [0,1] = [0,1]      1 * 1 = 1
[0,1] o [1,0] = [1,0]      1 * 5 = 5
[1,0] o [0,1] = [1,0]      5 * 1 = 5
[1,0] o [1,0] = [0,1]      1 * 1 = 1

As a result, the above are these for equations

f.


g.
The size of the two groups are not equal.
S5 has 5! permutations.
However (z/5z,+) does not have that much permutations
As a result, there can be no isomorphism betweeb to algebraic structures.






'''


## takes two arguments: a permutation p (represented as a Python list of integers) and a list l of the same length as the permutation.
## It should return the list after it has been permuted according to the permutation.
def permute(p,l):
    A =[ 0 for x in range(len(p))]
    for i in range(len(p)):
         A[i] = l[p[i]]
    return A


## takes two integers k and m where k < m and returns the cyclic permutation in Cm that shifts all elements up by k.
def C(k,m):
 A = [ x for x in range(m)]

 for i in range(len(A)):
     A[i] = A[i] + k
     if A[i]>=m:
         A[i] = A[i] - m 
 return A

def M(a,m):
    A = [ 0 for x  in range(m)]
    for i in range(m):
        A[i] = a*i%(m)

    return A


## the fucntion returns a permutaiton if it sorts the lists in asending order.
def sort(l):
    A = sorted(l)
    P = [0 for x  in range(len(l))]
     ## get the permutation
    for i in range(len(l)):
        for j in range(len(l)):
            if A[i] == l[j]:
                P[i] = j
  
   ## check if P is Cyllic Permuation
    if P == C(P[0],len(l)):
        return P
   ## check if P is mutiplication-induced Permutation
    a = (P[1]+len(l))
    if P == M(a,len(l)):
        return P
    else:
        return None

def unreliableUntrustedProduct(xs, n):
    url = 'http://cs-people.bu.edu/lapets/235/unreliable.php'
    return int(urlopen(url+"?n="+str(n)+"&data="+",".join([str(x) for x in xs])).read().decode())




# Code from last homework( get mutiplicative inverse)
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


#  return a single integer: the RSA ciphertext c.
def encrypt(m,t):
    c = pow(m,t[1], t[0])
    return c

# It should decrypt c and return the original message m.
def decrypt(c,t):
    m = pow(c,t[1],t[0])
    return m



 ## takes three inputs: a non-empty list of integers xs, a prime p, and another distinct prime q. The function must compute
 ## the product modulo p of all the integers in the list xs
def privateProduct(xs,p,q):
    n = p*q
    phi_n = (p-1)*(q-1)
    e = randint(2,phi_n-1)
    while gcd(e,phi_n) != 1:
        e = randint(2,phi_n-1)
    d = inv(e,phi_n)%phi_n
    for i in range(len(xs)):
        xs[i] = encrypt(xs[i],[n,e])

    A = unreliableUntrustedProduct(xs, n)
    A1 = decrypt(A,[n,d])
    return  A1%p

## Implement a function validPrivateProduct(xs, p, q) that takes three inputs: a non-empty list of integers xs, a prime p, and another distinct prime q. The function must always correctly compute the
## product modulo p of all the integers in the list xs
def validPrivateProduct(xs,q,p):
    n = p*q
    phi_n = (p-1)*(q-1)
    e = randint(2,phi_n-1)
    while gcd(e,phi_n) != 1:
        e = randint(2,phi_n-1)
    d = inv(e,phi_n)%phi_n
    r = randint(1,q-1)
    for i in range(len(xs)):
        xs[i] = (xs[i]*p*inv(p,q)+r*q*inv(q,p))%(p*q)
       
    for i in range(len(xs)):
        xs[i] = encrypt(xs[i],[n,e])
    A = unreliableUntrustedProduct(xs, n)
    A1 = decrypt(A,[n,d])         ##decrypt value
    A2 = A1%q
    answer = A1%q%p
    while A2 != pow(r,len(xs),q):
        r = randint(1,q-1)
        for i in range(len(xs)):
            xs[i] = (xs[i]*p*inv(p,q)+r*q*inv(q,p))%(p*q)
        for i in range(len(xs)):
            xs[i] = encrypt(xs[i],[n,e])
            A = unreliableUntrustedProduct(xs, n)
            A1 = decrypt(A,[n,d])         ##decrypt value
            A2 = A1%q
            answer=A1%q%p
    return answer
        





'''
Extra credit:
(z/8z)* = {1,5,7}
(z/10z)* = {1 ,3, 7, 9}

They do not have the same size. As a result, it cannot exist.
'''

 






    
        
