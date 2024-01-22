def suite_u(n) : # La fonction donnee dans la correction pour un
    u = 0
    for i in range(1,n+1):
        u = 5*u-8*n+6
    return u

#for i in range(1, 10):
    print(f"U{i} : ", suite_u(i))

def suite_v(n) : # La fonction donnee dans la correction pour vn
    u = 0
    for i in range(1,n+1):
        u = 5*u-8*n+6
    return u-2*n+1

#for i in range(1, 10):
    print(f"V{i} : ", suite_v(i))

def su(n): # Ma proposition pour Un, qui renvoie su(0) = u1, su(1) = u2, etc...
    u = 6
    for i in range(1, n+1):
        u = 5*u - 8*i + 6
    return u

for i in range(1, 10):
    print(f"U{i} : ", su(i))

def sv(n): # Ma proposition pour Vn, qui renvoie sv(0) = v1, sv(1) = v2, etc...
    v = 1
    for i in range(1,n+1):
        v = su(i) -2*n-1 # ou su(i) - 2 * i -1
    return v

for i in range(1, 10):
    print(f"V{i} : ", sv(i))
