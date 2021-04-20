from mxnet import np, npx

npx.set_np()

# x = np.array(3.0)
# y = np.array(2.0)
#
# print(x+y, x*y, x/y, x**y)
# print(type(x))
# print(type(y))

# x = np.arange(4)
# print(x)
# print(x[3])
# print(len(x))
# print(x.shape)

# X = np.arange(20).reshape(5, 4)
# print(X)
# print(X.T)

# X = np.arange(24).reshape(4, 3, 2)
# print(X)
# print(X[0][1][1])

# Properties of tensor arithmetic
A = np.arange(24).reshape(2, 3, 4)
B = A.copy() # Shallow copy

print(A)
print(B)
print(A+B)
print((A+B).shape)
print(A*B) #This gives us the Hadamard Product
print((A*B).shape)
print(A+2)
print((A+2).shape)