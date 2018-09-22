#This is the code for the avocado prices prediction code
#@author Lynn Mumia


#importing all the needed packages
import csv
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt


#Reading the data into a dataframe
avocado= pd.read_csv('C:/Users/Lynn/Desktop/Inclusive/inclusiveProject/avocado-prices/avocado.csv')
#print (avocado)

#Doing Exploratory dat analysis on the data set
print (avocado.shape)

#Checking the first and last data fields 
avocado.head(3)
avocado.tail(5)

#Checking for important statistics details for the numeric variables
avocado.describe()


#Checking null values
avocado.isnull().values.any()
