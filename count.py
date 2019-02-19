
s = input() + "0"
p = []
i = 0
j = 1
c = 1
if len(s) == 2:
  print(s[0] + "1")



print(''.join(str(x) for x in p))



###


s = input()
def count_char(string1):
    string2 = ""
    lst=[]
    lst1=[]
    for i in string1:
        count=0
        if i not in lst:
            for j in string1:
                if i==j:
                    count+=1
            lst1.append(i)
            lst1.append(count)
            lst.append(i)
    string2=''.join(str(x) for x in lst1)
    return string2
print(count_char(s))


######

s = input() + "0"
p = []
i = 0
j = 1
c = 1
if len(s) == 2:
  print(s[0] + "1")
else:
  for j in range(1, len(s)-1):
      if s[i] == s[j]:
        p.append(s[i])
        while s[i] == s[j]:
          c += 1
          j += 1
          if j == len(s):
            break
        p.append(c)
        i += c
        #break
      else:
        if s[i] != s[j]:
            while j < len(s)-1:
                c = 1
                i += 1
                j += 1
                p.append(s[j-1])
                p.append(c)
  print(''.join(str(x) for x in p))
