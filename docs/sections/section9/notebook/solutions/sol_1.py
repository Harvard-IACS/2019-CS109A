w1 = 2
b1 = 0.0
w2  = 1
b2  = 0.5

# affine operation
l1 = w1*x_train + b1
# activation
h = g(l1)
# output linear layer
y_model = w2*h + b2

