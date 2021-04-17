from mxnet import np, npx

npx.set_np()

x = np.array(3.0)
y = np.array(2.0)

print(x+y, x*y, x/y, x**y)
print(type(x))
print(type(y))