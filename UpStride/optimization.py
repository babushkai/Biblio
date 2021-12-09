import random

def nn(w,x,b):
    return w*(x**2) + b

w = random.random()
b = random.random()
lr = 0.1

x = 2S
y = 0


def update_params():
    global w, b
    y_pred = nn(w,x,b)
    print(y_pred)
    derivative_wrt_w = -2*x**2*(y - y_pred)
    derivative_wrt_b = -2*(y - y_pred)
    w = w - lr*derivative_wrt_w
    b = b - lr*derivative_wrt_b

for i in range(1000):
    _y = nn(w,x,b)
    dy = y - _y
    
