s = input()
L = "([{"
R = ")]}"
stack = []
err = False
count = 0
for c in s:
    if c in L:
        stack.append(c)
        count += 1
    p = R.find(c)
    if p >= 0:
        if not stack:
            err = True
            count += 1
        else:
            top = stack.pop()
            count += 1
            if p!= L.find(top):
                err = True
    if err: break

if not err:
    print ( "Success" )
else:
    if len(stack) > 0:
        print(count)
    else:
        print(count)
