import numpy as np
from fractions import Fraction
def dis(vect, deci):
 return np.round((vect).astype(float), decimals=deci)
my_dp = Fraction(1, 3)
mat = np.matrix([[0, 0, 1], [Fraction(1, 2), 0, 0], [Fraction(1, 2), 0, 0]])
ex = np.zeros((3, 3))
ex[:] = my_dp
beta = 0.7
a1 = beta * mat + ((1 - beta) * ex)
r = np.matrix([my_dp, my_dp, my_dp])
r = np.transpose(r)
prev = r
for i in range(1,100):
 r = a1*r
 print(dis(r, 3))
 if (prev == r).all():
  break
 prev = r
print("Final:", dis(r, 3))
print("sum:", np.sum(r))