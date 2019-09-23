def best_fit_line_scratch(x, y, b0, b1, title):
    # font size
    f_size = 18
    
    best_fit = b0 + b1 * x
    
    # make the figure
    fig, ax = plt.subplots(1,1, figsize=(8,5)) # Create figure object

    # set axes limits to make the scale nice
    ax.set_xlim(np.min(x), np.max(x) + 1)
    ax.set_ylim(np.min(y), np.max(y) + 1)

    # adjust size of tickmarks in axes
    ax.tick_params(labelsize = f_size)
    
    # adjust size of axis label
    ax.set_xlabel(r'$x$', fontsize = f_size)
    ax.set_ylabel(r'$y$', fontsize = f_size)
    
    # set figure title label
    ax.set_title(title, fontsize = f_size)

    # you may set up grid with this 
    #ax.grid(True, lw=1.75, ls='--', alpha=0.15)

    # draw best fit line (Notice the label argument!)
    ax.plot(x, best_fit, ls='--', label=r'$best\;fit$')

    ax.scatter(x, y)
    
    ax.legend()
    ax.legend(loc='best', fontsize = f_size);
    
    return ax
