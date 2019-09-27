titanic_train['sex_male'] = (titanic_train.sex == 'male').astype(int)
titanic_train['sex_male'].value_counts()