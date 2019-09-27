model_2 = sm.OLS(titanic_train['fare'], 
                 sm.add_constant(titanic_train[['age', 'sex_male', 'class_Second', 'class_Third']])).fit()
model_2.summary()