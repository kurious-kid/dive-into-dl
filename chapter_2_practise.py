from mxnet import np, npx
npx.set_np()

# Stuff about np
# x = np.arange(12)
# print("x: ", x)
# print("x.shape: ", x.shape)
# print("x.size: ", x.size)
# X = x.reshape(3, 4)
# print("reshaped X: ", X)
# print("X.shape: ", X.shape)
# print("np.zeros: ", np.zeros((2,3,4)))

# Stuff about tensors. Trying to wrap my head around more than two dimensions in tensors.
# random_tensor = np.random.normal(0, 1, (2,3,4))
# print("random_tensor: ",  random_tensor)
# print("random tensor[0][0][0]: ", random_tensor[0][0][0])
# print("random tensor[0][0][1]: ", random_tensor[0][0][1])
# print("random tensor[1][1][1]: ", random_tensor[1][1][1])
# print("random_tensor.shape: ", random_tensor.shape)

# Elementwise operations:
# x = np.array([1, 2, 4, 8])
# y = np.array([2, 2, 2, 2])
#
# print("x +y: ",  x+y)
# print("x-y: ",  x-y)
# print("x*y: ",  x*y)
# print("x/y: ",  x/y)
# print("np.exp(x): ", np.exp(x))

# Concatenating of tensors

# X = np.arange(12).reshape(3,4)
# Y = np.random.normal(0,1,(3,4))
# print("X",X)
# print("Y",Y)
# print("np.concatenate([X,Y], axis=0)", np.concatenate([X,Y], axis=0), np.concatenate([X,Y], axis=0).shape)
# print("np.concatenate([X,Y], axis=1)", np.concatenate([X,Y], axis=1), np.concatenate([X,Y], axis=1).shape)

# Saving memory
# Z = np.zeros_like(Y)
# print("Before slice: ", id(Z))
#
# Z[:] = X + Y
# print("After slice: ", id(Z))
#
# Z = X + Y
# print("without slice: ", id(Z))
# print(type(id(Z)))

# Data pre-processing

# creating a CSV
import os
#
# os.makedirs(os.path.join("data"), exist_ok=True)
# data_file = os.path.join("data", "house_tiny.csv")
# with open(data_file, 'w') as f:
# 	f.write('NumRooms, Alley,Price\n')
# 	f.write('NA,Pave,1234\n')
# 	f.write('2,NA,5678\n')

import pandas as pd

data = pd.read_csv(os.path.join("data", "house_tiny.csv"))
print(data)