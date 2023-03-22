# Polynomial Fit for Test Scores Prediction

This repository contains a Python script that demonstrates how to fit a polynomial model to a given dataset and use it for predicting test scores based on the number of hours spent studying.

## Dependencies

The following Python packages are required:

- NumPy
- Matplotlib
- scikit-learn

To install the required packages, run:

```bash
pip install numpy matplotlib scikit-learn
```

or

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository

```bash
git clone https://github.com/codecaine-zz/polynomial_fit.git
```

2. navigate project folder

```bash
cd polynomial_fit
```

3. run script

```bash
python polynomial_fit.py
```

The script will output an R2 score and a predicted test score for a given number of hours spent studying. It will also generate a plot showing the original data and the fitted polynomial curve.

## Example

In this example, we have a dataset of hours spent studying and the corresponding test scores:

- x: Hours spent studying
- y: Test scores

The script fits a polynomial model to the data, plots the data with the fitted line, and predicts the test score for a given number of hours spent studying. The R2 score is calculated to evaluate the model's performance.