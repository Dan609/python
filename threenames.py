a = 'dead'
b = 'parrot'
c = 'sketch'
print (a, b, c)

import time
start_time = time.time()
s = 0
for x in range(1,1000001):
    s += x*x
print("Sum={}, T={}s".format(s, time.time() - start_time))
