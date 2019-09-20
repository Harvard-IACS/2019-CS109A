
# First get the data
f = logistic(x, 2.0, 1.0)
g = stretch_tanh(x, 2.0, 0.5, 0.5)
h = relu(x)

fig, ax = plt.subplots(2,3, figsize=(20,6)) # Create figure object

# Make actual plots
ax[0][0].plot(x, f, lw=4, ls='-', label=r'$L(x;1)$')
ax[1][1].plot(x, g, lw=4, ls='--', label=r'$\tanh(2x)$')
ax[1][2].plot(x, h, lw=4, ls='-.', label=r'$relu(x; 0.01)$')
