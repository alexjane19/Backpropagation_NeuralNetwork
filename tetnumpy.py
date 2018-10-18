from numpy import array
from numpy import dot,sign
from stemming.porter2 import stem
a = "exported"
c = stem(a)
print(c)
# weights = array(array([0] * 5))
# wt = array(array([1] * 5))
#
# xt = [0] * 100
# pt = [0]* 100
# x = sign(dot(xt, pt))
# print(x)
# y = dot(weights, wt)
#
# print(y)
#
# test = [1,2,3,4,5,6,7,8,9]
# for i in range(0,len(test),4):
#     print(test[i:i+4])
#

