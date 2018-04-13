#!/usr/bin/env python3

# import csv
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler 
from sklearn.neural_network import MLPClassifier  
from sklearn.metrics import classification_report, confusion_matrix  
from sklearn.feature_selection import RFE

def main():
    data = pd.read_csv("Converted_Datasets/trimmed.csv", sep=',', quotechar='"')
    data.set_index('IRN', inplace=True)

    # Assign data from first four columns to X variable
    X = data.iloc[:, 1:12]

    # Assign data from first fifth columns to y variable    
    y = data.iloc[:, 13:]

    # le = preprocessing.LabelEncoder()
    # y = y.apply(le.fit_transform)  
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)  
     
    scaler = StandardScaler()  
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)  
    X_test = scaler.transform(X_test) 
    
    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)  
    mlp.fit(X_train, y_train.values.ravel())   

    predictions = mlp.predict(X_test) 

    print(mlp.score(X, y))
    print(confusion_matrix(y_test,predictions))  
    print(classification_report(y_test,predictions)) 

# create the RFE model and select 3 attributes
# rfe = RFE(model, 3)
# rfe = rfe.fit(dataset.data, dataset.target)
# # summarize the selection of the attributes
# print(rfe.support_)
# print(rfe.ranking_)

    rfe = RFE(mlp, 11)
    rfe = rfe.fit(X_train, y_train)

    # print(rfe.support_)
    print(rfe.ranking_)


main()
    