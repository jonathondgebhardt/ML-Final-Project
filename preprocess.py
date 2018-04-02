#!/usr/bin/env python3

#
# TODO: Normalize data. Operating expenditures blows everything out of proportion
# when everything is plotted.
#


#
# CRI: Percentage spent on classroom instruction
# NCR: Percentage spent on non-classroom
# ADM: Average Daily Membership
#


import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # Print list of matching IRNs
# def printLookups(irn_list):
#     for i in irnLookups:
#         print (i, irnLookups.get(i))

# for county in irnLookups:
#     temp = irnLookups.get(county)
#     print (county, '(', len(temp), ')\n\t', irnLookups.get(county))


def main():
    data = pd.read_csv("expanded_intersection_trimmed.csv", sep=',', quotechar='"')
    # print(data.describe())
    # print(data.shape)
    data.set_index('IRN', inplace=True)

    # Get one column by name
    #montgomeryData = data.loc[data['County Name'] == 'Montgomery']

    #print(montgomeryData.describe())
    
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    data_numerics = data.select_dtypes(include=numerics)
    data_numerics_norm = (data_numerics - data_numerics.mean()) / (data_numerics.max() - data_numerics.min())

    # print(data_numerics_norm.describe())

    data_numerics_norm.hist()
    plt.show()

    # data.hist(column = 'County Mortality Rate') 
    # plt.show()

    # X = data_numerics_norm.iloc[:, :2]
    # Y = data_numerics_norm.iloc[:, 17:]

    #print(X)
    #print(Y)

    # plt.scatter(X, Y)
    # plt.show()

    # print(X.head())
    # print(Y.head())


main()
    