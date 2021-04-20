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
# A = np.arange(24).reshape(2, 3, 4)
# B = A.copy() # Shallow copy
#
# print(A)
# print(B)
# print(A+B)
# print((A+B).shape)
# print(A*B) #This gives us the Hadamard Product
# print((A*B).shape)
# print(A+2)
# print((A+2).shape)

# Reduction (refers to reduction of axis when summmed along it
# x = np.arange(4)
# print(x.sum())

A = np.arange(20).reshape(5, 4)
# print(A.sum())

print(A)

# A_sum_along_axis_0 = A.sum(axis=0)
# print(A_sum_along_axis_0)
# print(A_sum_along_axis_0.shape)
#
# A_sum_along_axis_1 = A.sum(axis=1)
# print(A_sum_along_axis_1)
# print(A_sum_along_axis_1.shape)
#
# A_sum_along_all_axes = A.sum(axis=[0, 1])
# print(A_sum_along_all_axes)
# print(A_sum_along_all_axes.shape)
#
# print(A.mean())
# print(A.sum()/A.size)
#
# print(A.mean(axis=0))
# print(A.sum(axis=0)/A.shape[0])

# Non-reduction sum
# sum_A = A.sum(axis=1, keepdims=True)
# sum_A_withput_dims = A.sum(axis=1)
# print(sum_A)
# print(sum_A.shape)
#
# print(sum_A_withput_dims)
# print(sum_A_withput_dims.shape)
#
# sum_B = A.sum(axis=0, keepdims=True)
# sum_B_without_dims = A.sum(axis=0)
# print(sum_B)
# print(sum_B.shape)
# print(sum_B_without_dims)
# print(sum_B_without_dims.shape)
#
# print(A/sum_B)
# print((A/sum_B).shape)
#
# print(A/sum_B_without_dims)
# print((A/sum_B_without_dims).shape)

# sum_C = A.sum(axis=[0, 1], keepdims=True)
# sum_c_without_dims = A.sum(axis=[0, 1])
#
# print(sum_C)
# print(sum_C.shape)
# print(sum_c_without_dims)
# print(sum_c_without_dims.shape)
#
# print(A/sum_c_without_dims)
# print(A/sum_C)

print(A.cumsum(axis=0))
print(A.cumsum(axis=1))

