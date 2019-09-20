# First get the data
f = logistic(x, 2.0, 1.0)
g = stretch_tanh(x, 2.0, 0.5, 0.5)
h = relu(x)

fig, ax = plt.subplots(1,3, figsize=(20,6)) # Create figure object

# Make actual plots
ax[0].plot(x, f, lw=4, ls='-', label=r'$L(x;1)$')
ax[1].plot(x, g, lw=4, ls='--', label=r'$\tanh(2x)$')
ax[2].plot(x, h, lw=4, ls='-.', label=r'$relu(x; 0.01)$')

# Make the tick labels readable
ax[0].tick_params(labelsize=24)
ax[1].tick_params(labelsize=24)
ax[2].tick_params(labelsize=24)

# Set axes limits to make the scale nice
ax[0].set_xlim(x.min(), x.max())
ax[0].set_ylim(h.min(), 1.1)
ax[1].set_xlim(x.min(), x.max())
ax[1].set_ylim(h.min(), 1.1)
ax[2].set_xlim(x.min(), x.max())
ax[2].set_ylim(h.min(), 1.1)

# Make readable labels
ax[0].set_xlabel(r'$x$', fontsize=24)
ax[0].set_ylabel(r'$h(x)$', fontsize=24)
ax[0].set_title('Activation Functions', fontsize=24)

ax[1].set_xlabel(r'$x$', fontsize=24)
ax[1].set_ylabel(r'$h(x)$', fontsize=24)
ax[1].set_title('Activation Functions', fontsize=24)

ax[2].set_xlabel(r'$x$', fontsize=24)
ax[2].set_ylabel(r'$h(x)$', fontsize=24)
ax[2].set_title('Activation Functions', fontsize=24)

# Set up grid
ax[0].grid(True, lw=1.75, ls='--', alpha=0.75)
ax[1].grid(True, lw=1.75, ls='--', alpha=0.75)
ax[2].grid(True, lw=1.75, ls='--', alpha=0.75)

# Put legend on figure
ax[0].legend(loc='best', fontsize=24);
ax[1].legend(loc='best', fontsize=24);
ax[2].legend(loc='best', fontsize=24);

#fig.savefig('../images/nice_sub_plots.png')
