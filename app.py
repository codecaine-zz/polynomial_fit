import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def plot_polynomial_fit(x, y, degree=3):
    # Fit the polynomial model
    mymodel = np.poly1d(np.polyfit(x, y, degree))
    myline = np.linspace(min(x), max(x), 100)

    # Calculate the R2 score
    r2 = r2_score(y, mymodel(x))

    # Plot the data and the fitted line
    plt.scatter(x, y)
    plt.plot(myline, mymodel(myline))
    plt.xlabel("Hours Studied")
    plt.ylabel("Test Score")
    plt.show()

    return mymodel, r2

# Hours spent studying
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]

# Test scores
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# Fit the polynomial model and plot the data
mymodel, r2 = plot_polynomial_fit(x, y)
print(f"R2 score: {r2:.2f}")

# Predict the test score for a given number of hours spent studying
hours_studied = 10
predicted_test_score = mymodel(hours_studied)
print(f"Predicted test score for {hours_studied} hours of studying: {predicted_test_score:.2f}")
