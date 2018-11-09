#This is the Avocado Prices prediction code
#@author Lynn Mumia


#importing all the needed packages
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import TimeGrouper
from pandas import DataFrame
from pandas import Series


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
#Average price= $1.4
#Maximum price= $3.25
#Minimum price= $0.44


#Labelling categorical columns in the data
avocado= avocado.astype(dtype={
    'type':'category','year':'category','region':'category'})

#Converting the date column to a datatime
avocado['Date']= pd.to_datetime(avocado['Date'], format='%Y-%m-%d')

#Sorting the data by date
avocado=avocado.sort_values(by='Date', ascending=True)


#Checking for null values
avocado.isnull().values.any()
#No null values found in the dataset

#Understanding categorical columns
categoricals_col = avocado.select_dtypes(include=['category']).copy()
categoricals_col.describe()

avocado.info()


#Plots to explore the volumes of avocadoes with respect to date
x=avocado['Date']
y=avocado['Total Volume']
plt.plot(style='k.')
plt.plot(x,y)
plt.show()

#plotting with dots instead of lines
#plt.plot(style='k.')
#plt.show()


#Working on the time series prediction model of dates versus the volume
from fbprophet import Prophet

#Fitting the model
p=Prophet()
p.fit(avocado-date,time)

#Making the future dataframe which will store the predicted values
avocadoFuture=p.make_future_dataframe(periods=365)
avocadoFuture(tail)

#Forecasting values
avocadoForecast= p.predict(avocadoFuture)
avocadoForecast[["ds","yhat","yhat_lower","yhat_upper"]].tail()

#plotting the forecast
avocadoForecastPlot=p.plot(avocadoForecast)

#plotting the forecast components
avocadoForecastComponentPlot= p.plot_components(avocadoForecast)
