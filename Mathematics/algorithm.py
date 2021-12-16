### Sort
num_list = [0, 6, 0, 2, 0, 1, 5]

for i in range(len(num_list)-1):
    for i in range(len(num_list)-1):
        if num_list[i]== 0:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

### Maximum common Divisor
a = 60
b= 48

def computeGCD(x, y):
   while(y):
       x, y = y, x % y
   return x

computeGCD(a, b)
