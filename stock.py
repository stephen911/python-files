import math
import pandas_datareader as web
import warnings
# This program predicts stock prices by using machine learning models

#Install the dependencies
import quandl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
#Get the stock data
df = quandl.get("WIKI/AMZN")
# Take a look at the data
print(df.head())