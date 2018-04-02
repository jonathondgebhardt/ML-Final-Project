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
    data = pd.read_csv("expanded_intersection.csv", sep=',', quotechar='"')
    
    # print(data.describe())
    
    # data.hist(xlabelsize=0, ylabelsize=0)
    # plt.show()

    # data.hist(column = 'County Mortality Rate') 
    # plt.show()

    X = data.iloc[:, 6:7]
    Y = data.iloc[:, 31:]

    

    plt.scatter(data.iloc[:, 6:7], data.iloc[:, 31:])
    plt.show()

    # print(X.head())
    # print(Y.head())


main()
    