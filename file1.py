import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

def build_model(X_train, y_train):
    poly_reg = PolynomialFeatures(degree = 2)
    X_poly = poly_reg.fit_transform(X_train)

    reg = LinearRegression()
    reg.fit(X_poly, y_train)

    return poly_reg, reg

def test_model(poly_reg, reg, X):
    X_poly = poly_reg.transform(X)
    predictions = reg.predict(X_poly)
    return predictions

# set the seed to make your partition reproducible
random_seed = 42
random.seed(random_seed)

# reading the data from the given raw file
df = pd.read_csv('DSDataLastThreeMonths.csv')

# removing null values for further analysis
df.dropna(inplace=True)
# removing unnecessary columns
df.drop(columns=["CASTNO"], inplace=True)

# extracting the independent variable, X
X = df.iloc[:,:-1].values
# extracting the dependent variable, y
y = df.iloc[:,-1].values

# splitting the entire dataset into test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state = 42)

# standardizing the data
sc = StandardScaler()
X_train[:,:] = sc.fit_transform(X_train[:,:])
X_test[:,:] = sc.transform(X_test[:,:])

# build model
poly_reg, reg = build_model(X_train,y_train)

# generate predictions on test and train dataset
pred_test = test_model(poly_reg, reg, X_test)
pred_train = test_model(poly_reg, reg, X_train)

#tolerance range
check = 0.002

# finding the error on the predictions
y_test = list(y_test)
y_train = list(y_train)
err_test = [x-y for x,y in zip(pred_test,y_test)]
err_train = [x-y for x,y in zip(pred_train,y_train)]

# finding the strike rates on the datasets
strike_rate_test = 100*sum([np.abs(x)<=check for x in err_test])/len(err_test)
strike_rate_train = 100*sum([np.abs(x)<=check for x in err_train])/len(err_train)

# printing the results
print("Test strike rate : {}\nTrain strike rate : {}".format(strike_rate_test,strike_rate_train))