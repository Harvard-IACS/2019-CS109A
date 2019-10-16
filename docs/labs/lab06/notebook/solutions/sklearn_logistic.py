from sklearn.linear_model import LogisticRegression

fitted_lr = LogisticRegression(C=1000000, solver='newton-cg', max_iter=250).fit(x_train,y_train)
print(fitted_lr.coef_)

print("Test set score:", fitted_lr.score(x_test,y_test))