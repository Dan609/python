a = [int(i) for i in input().split()]
#читает строку чисел, разделённых пробелами


print(sum(map(int, input().split())))
print(sum(list(map(int,input().split()))))
#напишите сумму чисел в этой строке

a = [int(i) for i in input().split()]
s = 0
for i in a:
    s += int(i)
print(s)
