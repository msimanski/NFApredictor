#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:54:23 2018

@author: michaelsimanski
"""

import pandas
from sklearn.linear_model import LinearRegression

pandas.set_option("display.max_rows", 500)

sourceFile = pandas.read_excel('transfers-purged-culled.xlsx')
namesFile = pandas.read_excel('examinercodes.xlsx')

def printFormTypes():
    print("F1 Individual = 1")
    print("F1 LLC/Corp = 2")
    print("F1 Trust = 3")
    print("F4 Individual = 4")
    print("F4 LLC/Corp = 5")
    print("F4 Trust = 6")
    print("Form 4 to Dealer = 7")

def printExaminerCodes():
    print(namesFile)

print("NFA PAPERWORK PREDICTION MAKER")
print("------------------------------")

menuIndex = 0

while menuIndex != 9:
    print("")
    print("Options:")
    print("1. Predict wait time based on examiner.")
    print("2. Predict wait time based on if you eFiled")
    print("3. Predict wait time based on form type")
    print("4. Predict wait time based on full hypothetical entry")
    print("9. Exit.")
    menuIndex = int(input("Option selection: "))
    # print(menuIndex)
    print("")
    
    if menuIndex == 1:
        Y = sourceFile[['Days between sent and received']]
        X = sourceFile[['Examiner name code']]
        model = LinearRegression()
        model.fit(X, Y)
        
        printExaminerCodes()
        
        nameCode = int(input("Examiner Name Code: "))
    
        X_predict = [[nameCode]]
        y_predict = model.predict(X_predict)
        
        print("It should take ", end = "")
        print(int(y_predict), end = "")
        print(" days with examiner ", end = "")
        print(nameCode)
        
    if menuIndex == 2:
        Y = sourceFile[['Days between sent and received']]
        X = sourceFile[['Efile']]
        model = LinearRegression()
        model.fit(X, Y)
        
        efiled = int(input("Enter 1 if eFiled, 0 if not: "))
        
        X_predict = [[efiled]]
        y_predict = model.predict(X_predict)
        
        print("It should take ", end = "")
        print(int(y_predict), end = "")
        print(" days ", end = "")
        if efiled == 1:
            print(" if you eFiled.")
        else:
            print("if you did not eFile.")
            
    if menuIndex == 3:
        printFormTypes()
        Y = sourceFile[['Days between sent and received']]
        X = sourceFile[['Form type code']]
        model = LinearRegression()
        model.fit(X, Y)
        
        formCode = int(input("Enter form type code: "))
        
        X_predict = [[formCode]]
        y_predict = model.predict(X_predict)
        
        print("It should take ", end = "")
        print(int(y_predict), end = "")
        print(" days with form code ", end = "")
        print(formCode)

    if menuIndex == 4:
        Y = sourceFile[['Days between sent and received']]
        X = sourceFile[['Examiner name code', 'Form type code', 'Efile']]
        model = LinearRegression()
        model.fit(X, Y)
        
        printExaminerCodes()
        nameCode = int(input("Examiner Name Code: "))
        
        efiled = int(input("Enter 1 if eFiled, 0 if not: "))
        
        printFormTypes()
        formCode = int(input("Enter form type code: "))
        
        X_predict = [[nameCode, efiled, formCode]]
        y_predict = model.predict(X_predict)
        
        if y_predict < 0:
            print("The hypothetical entry you described is not featured enough in the dataset to make a prediction. Please try another entry.")
        else:
            print("The hypothetical entry you described should take ", end = "")
            print(int(y_predict), end = "")
            print(" days to process.")