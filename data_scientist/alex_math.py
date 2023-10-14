import math

def sinus(x):
  sum = 0
  for n in range (0, 10):
    sum = sum + (-1)**n * x**(2*n+1) / math.factorial(2*n+1)
  return sum

print(sinus(1.23))
print(math.sin(1.23))
