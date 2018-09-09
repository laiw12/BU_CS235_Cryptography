# Name: Lai Wei
# Email: laiw12@bu.edu

# code from lecture
def forall(S, P):
    for x in S:
        if not P(x):
            return False
    return True
# code from lecture
def exists(S, P):
    for x in S:
        if P(x):
            return True
    return False

# code from lecture
def relation(R, X):
  return R.issubset(product(X, X))

# code from lecture
def subset(X,Y):
  return forall(X, lambda x: x in Y)

# code from lecture
def quotient(X, R):
    return {frozenset({y for y in X if (x,y) in R}) for x in X}

# code from lecture
def product(X, Y):
  return { (x,y) for x in X for y in Y }

def square(n):
    return exists(set(range(1,n+1)),lambda x :(x*x==n))

# helper function for squarefree(n)
def imply(x,y):
    return not x or y

def squarefree(n):
     return forall(set(range(2,n)), lambda x: imply(n%x==0,not square(x)))
    
def properSquareFactors (n):
    return { x for x in range(2,n) if n%x==0 and square(x)}

# helper function for shared
def sharedhelp(s,p):
    return exists(s,lambda x: x in p)

def shared(s):
    return {(x,y) for x in s if not squarefree(x) for y in s if sharedhelp(properSquareFactors(x),properSquareFactors(y)) }

# question 1.e

reflexive = None
symmetric = None
transitive = {12,18,36}


def isReflexive(X,R):
    return relation(R, X) and forall(X,lambda x: ((x,x) in R))

def isSymmetric(X,R):
     return relation(R,X) and forall(X,lambda x: forall(X,lambda y:((x,y) in R) <= ((y,x) in R)))

def isTransitive(X,R):
    return  relation(R,X) and forall(X,lambda x: forall(X,lambda y:forall(X,lambda z:(((x,y) in R) and (y,z) in R) <=((x,z) in R))))                 

def isEquivalence(X,R):
    return relation(R,X) and isReflexive(X,R) and isSymmetric(X,R) and isTransitive(X,R)
    
X1 = {"a","b","c","d","e","f"}
R1 = {("a","a"),("b","b"),("c","c"),("a","b"),("b","a"),("b","c"),("c","b"),("a","c"),("c","a"),("f","f"),("d","d"),("f","d"),("d","f"),("e","e")}

X2 = {0,1,2,3,4,5,6,7,8,9,10,11}
R2 = {(0,0),(5,5),(10,10),(0,5),(5,0),(5,10),(10,5),(0,10),(10,0),(1,1),(11,11),(6,6),(1,11),(11,1),(11,6),(6,11),(1,6),(6,1),(7,7),(2,2),(7,2),(2,7),(3,8),(8,3),(3,3),(8,8),(4,9),(9,4),(4,4),(9,9)}


X3 = set(range(0,50))
R3 = product(set(range(0,25)),set(range(0,25)))| product(set(range(25,50)),set(range(25,50)))





