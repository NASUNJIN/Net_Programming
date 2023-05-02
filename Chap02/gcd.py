def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(16, 24))

def pr(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        a, b = b, a % b

    return a

print(pr(16, 24))