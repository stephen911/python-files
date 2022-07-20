# importing numpy, matplotlib and skilearn libraries
import matplotlib_prac.pyplot as plt
import numpy as np

# importing datasets from scikit-learn
from sklearn import datasets, linear_model

# load the dataset
house_price = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
size = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]

# Reshape the input to your regression
size2 = np.array(size).reshape((-1, 1))
print(size2)

regr = linear_model.LinearRegression()
regr.fit(size2, house_price)

print("Coefficients:\n", regr.coef_)
print("Intercept:\n", regr.intercept_)

# Formula obtained for the trained model


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)


size_new = 1400
price = (size_new * regr.coef_) + regr.intercept_
price2 = regr.predict([[size_new]])
print(price2)
print(price)

graph("regr.coef_ * x + regr.intercept_", range(1000, 2700))
plt.scatter(size, house_price, color="black")
plt.ylabel("House Price")
plt.xlabel("Size of house")
plt.show()

