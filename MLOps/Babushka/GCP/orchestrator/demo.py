test = [2,4,1,2,0,2,4,0,2,3,0,2,0,0,0]

for i in range(len(test)-1):
    for j in range(len(test)-1):
        if test[j] == 0:
            test[j], test[j + 1] = test[j+1], test[j]
            

def gcd(a,b):
    if b == 0:
        return a
    
    gcd(b, a%b)
    

a, b, c = (4, 20), (20, 4), (0, 4)
    




