model = sm.OLS(y_train, x_train_ca)
results = model.fit()
print(results.params)