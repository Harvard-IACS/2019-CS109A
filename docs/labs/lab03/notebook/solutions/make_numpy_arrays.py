# make numpy arrays
x_data = np.array([1,2,3,5])
y_data = np.array([2,2,4,6])

#check type
print(type(x_data))

# compute the min and max
y_min, y_max = np.min(y_data), np.max(y_data)
x_min, x_max = np.min(x_data), np.max(x_data)

print(f'x_min = {x_min}, y_min = {y_min}, x_max = {x_max}, y_max = {y_max}')
