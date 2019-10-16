from sklearn.linear_model import LogisticRegression

fitted_lr = LogisticRegression(C=1000000, solver='newton-cg', max_iter=250).fit(x_train,y_train)
print("Coefficients:")
print(fitted_lr.coef_)
print("Intercepts:")
print(fitted_lr.intercept_)
