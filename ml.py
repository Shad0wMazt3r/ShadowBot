import matplotlib as plt
import numpy as np
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes() 
diabetes_X = diabetes.data[:, np.newaxis,2]

# print(diabetes_X)

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test  = diabetes_X[:-30]