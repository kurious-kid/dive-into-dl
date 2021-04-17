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
# 	f.write('3,Strut,5678\n')

import pandas as pd

# data = pd.read_csv(os.path.join("data", "house_tiny.csv"))
# # print(data)
#
# inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
# inputs = inputs.fillna(inputs.mean())
# # print(inputs)
#
# inputs = pd.get_dummies(inputs, dummy_na=True)
# # print(inputs)
#
# X, y = np.array(inputs), np.array(outputs)
# print(X)
# print(type(X))
# print(y)
# print(type(y))

# Exercise after 2.2.3
exercise_data_file = os.path.join("data", "exercise_data.csv")
# with open(exercise_data_file, 'w') as f:
# 	f.write("Name,Age,Gender,Height,Weight,Diabetes\n")
# 	f.write("Ankit,25,M,187,79,N\n")
# 	f.write("Ankit2,NA,M,123,NA,N\n")
# 	f.write("ANkit3,45,F,NA,NA,Y\n")
# 	f.write("Ankit4,25,M,187,79,N\n")
# 	f.write("Ankit5,NA,M,123,NA,N\n")
# 	f.write("ANkit6,45,F,NA,NA,Y\n")

exercise_data_import = pd.read_csv(exercise_data_file)
print(exercise_data_import)
# print(type(exercise_data_import))
# getting the columns with most number of NAs
column_with_most_nas = exercise_data_import.count().idxmin()
# eliminating the column with most NANs
exercise_data_import = exercise_data_import.drop(column_with_most_nas, axis=1)
print("after dropping")
print(exercise_data_import)
# getting rid of NANs
inputs, outputs = exercise_data_import.iloc[:, 0:4], exercise_data_import.iloc[:, 4]
inputs = inputs.fillna(inputs.mean())
print(inputs)
print(outputs)

inputs = pd.get_dummies(inputs, dummy_na=True)
outputs = pd.get_dummies(outputs, dummy_na=True)

print(inputs.columns)

print(outputs.columns)

print("type(inputs): ",type(inputs))
print("type(outputs): ",type(outputs))

print("input after get dummies\n", inputs)
print("output after get dummies\n", outputs)

inputs = np.array(inputs)
outputs = np.array(outputs)

print("type(inputs): ", type(inputs))
print("type(outputs): ", type(outputs))

print("after conversion to tensor\n")
print(inputs, "\n", inputs.shape)
print(outputs, "\n", outputs.shape)

# Linear Algebra




