# multiplication table

a, b, c, d = 7, 10, 5, 6

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

print(" ", *range(c, d+1), sep="\t")

for y in range(a, b+1):
    print(y, end='')
    for z in range(c, d+1):
        print("\t", "%2d" %(y*z), end='')
    print ("")


for row in range(a,b+1):
    print(*("{:3}".format(row*col) for col in range(c, d+1)))


print()
print("Think, then relax...")
print()

n=int(input('Please enter a positive integer between 1 and 15: '))
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col, end="\t")
    print()

import time

n=int(input('Please enter a positive integer between 1 and 15: '))
print()
print('Ok, printing multiplication table: ')
print()
for row in range(1,n+1):
    print(*("{:3}".format(row*col) for col in range(1, n+1)))
    time.sleep(0.3)

# Square

for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print(' ', end=' ')
    # Count up
    for j in range(1, i+1):
        print(j, end=' ')
    # Count downs
    for j in range(i-1, 0, -1):
        print(j, end=' ')
    # Next row
    print()
for i in range(10):
    # Print leading spaces
    for j in range(i+2):
        print(' ', end=' ')
    # Count up
    for j in range(1, 9-i):
        print(j, end=' ')
    # Count down
    for j in range(7-i, 0, -1):
        print(j, end=' ')
    print()

# Triangles

for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print(' ', end=' ')
    # Count up
    for j in range(1, i+1):
        print(j, end=' ')
    # Count down
    for j in range(i-1, 0, -1):
        print(j, end=' ')
    # Next row
    print()
print()
for row in range(10):
    for j in range(row):
        print(' ', end=' ' )
    for j in range(10-row):
        print(j, end=' ')
    print()

# Pascals triangles

def choose(n, k): # note no dependencies on any of the prior code
     if k in (0, n):
         return 1
     return choose(n-1, k-1) + choose(n-1, k)

for row in range(13):
    for k in range(row + 1):
        # flush is a Python 3 only argument, you can leave it out,
        # but it lets us see each element print as it finishes calculating
        print(choose(row, k), end=' ', flush=True)
    print()

#
def gen(n,r=[]):
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r
def draw(n):
    for p in gen(n):
        print(' '.join(map(str,p)).center(n*2)+'\n')
draw(10)

# Beautiful triangle

def draw_beautiful(n):
    ps = list(gen(n))
    max = len(' '.join(map(str, ps[-1])))
    for p in ps:
        print(' '.join(map(str,p)).center(max)+'\n')
draw_beautiful(24)
