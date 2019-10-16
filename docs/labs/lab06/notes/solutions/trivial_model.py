dumb_prediction = np.ones(len(y_test))
np.sum(y_test == dumb_prediction) / len(y_test)