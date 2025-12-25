# Regression between book's page and its price
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([500, 700, 800, 600, 400, 500, 600, 800]).reshape((-1, 1)) # page
y = np.array([84, 75, 99, 72, 69, 81, 63, 93]) # price

# Create the model
model = LinearRegression().fit(x, y)

# Get results
rsq = model.score(x, y)
print("rsq =", rsq)
print("Slope =", model.coef_)
print("Intercept =", model.intercept_)
