
import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Вывод всех простых чисел от 1 до N
N = 100
for p in range(1, N, 2):
    if is_prime(p): print(p)

# Вывод результата, является ли заданное число простым
print(is_prime(2147483647))
