# The smaller the `a`, the sharper the function is. 
# Variable `c` moves the function along the x axis 
def sigmoid(x,c,a):
    z = ((x-c)/a)
    return 1.0 / (1.0 + np.exp(-z))

x = np.linspace(-5.0, 5.0, 500) # input points
c = 1.
a = 0.5
plt.plot(x, sigmoid(x, c, a), label='sigmoid')
plt.plot(x, np.tanh(x), label='tanh')
plt.grid();
plt.legend();
