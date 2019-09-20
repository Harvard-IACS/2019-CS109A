A = np.array([ [5, 4, 3, 2, 1], [1, 2, 3, 4, 5], [1.1, 2.2, 3.3, 4.4, 5.5] ])
print(A, "\n")

# set length(shape)
dims = A.shape
print(dims, "\n")

# slicing
print(A[-1, 2:], "\n")
print(A[1:3, 3:5], "\n")

# square
A2 = A * A
print(A2)
