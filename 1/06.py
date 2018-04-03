def n_gram(size,string):
    mogi = []
    for i in range(0,len(string) - 1):
        mogi.append(string[i:i+size:1])
    return mogi

def Union(X,Y):
    Z = set(X) | set(Y)
    return Z

def Intersection(X,Y):
    Z = set(X) & set(Y)
    return Z

def Difference(X,Y):
    Z = set(X) - set(Y)
    return Z

X_string = "paraparaparadise"
Y_string = "paragraph"
X = n_gram(2,X_string)
Y = n_gram(2,Y_string)
print(Union(X,Y))
print(Intersection(X,Y))
print(Difference(X,Y))

check_se = Union(X,Y)

if  "se" in check_se:
    print("Found se")
else:
    print("Not found")