age_ca = sm.add_constant(titanic_train['age'])
model_1 = OLS(titanic_train['fare'], age_ca).fit()
model_1.summary()