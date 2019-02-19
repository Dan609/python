n = int(input())
if n>100 and 11<=n%100<=20:
    print(str(n) + ' программистов')
elif n == 1 or (n >= 21 and n%10==1):
    print(str(n) + ' программист')
elif 2<=n<=4 or (n>20 and 2<=n%10<=4):
    print(str(n) + ' программиста')
elif 5<=n<=20 or (n>20 and 5<=n%10<=9) or n%10==0:
    print(str(n) + ' программистов')
