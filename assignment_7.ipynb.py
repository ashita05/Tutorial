#1.create a random array with 10 elements n find thier mean
import numpy
arr = numpy.random.rand(10,1)
m = numpy.mean(arr)
print(arr)
print("mean =",m)

#2.find variance and standard deviation
import numpy
r = numpy.random.rand(20,1)
s = numpy.std(r)
v = numpy.var(r)
print(r)
print("standard deviation:",s)
print("variance:",v)

#3.mutliply 2 matrices n print the resultant matrix
import numpy
a = numpy.random.rand(10,20)
print("A is:",a)
b = numpy.random.rand(20,25)
print("B is:",b)
mul = numpy.matmul(a,b)
print("multiplication of 2 matrices is:",mul)
s = sum(mul)
print("sum of elements of new matrix",s)