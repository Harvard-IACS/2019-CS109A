titanic_train['age^2'] = titanic_train['age'] **2
model_5 = sm.OLS(
    titanic_train['fare'],
    sm.add_constant(titanic_train[['age', 'sex_male', 'class_Second', 'class_Third', 'sex_male_X_age', 
                             'sex_male_X_class_Second', 'sex_male_X_class_Third', 'age^2']])
).fit()
model_5.summary()