plt.scatter(range(1,11),np.cumsum(pca_10_transformer.explained_variance_ratio_))
plt.xlabel("PCA Dimension")
plt.ylabel("Total Variance Captured")
plt.title("Variance Explained by PCA");