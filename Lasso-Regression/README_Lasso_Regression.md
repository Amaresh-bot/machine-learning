# 📘 Lasso Regression – Effect of Regularization (α)

This project demonstrates how **Lasso Regression (L1 Regularization)** affects a regression model when applied with different **alpha (regularization) values**.  
The dataset is **synthetic**, generated using scikit-learn’s `make_regression`.  
A **Linear Regression** model is used as the baseline for comparison.

---

## ✅ Project Overview

This notebook performs the following steps:

1. **Import required libraries**  
   (`numpy`, `pandas`, `matplotlib`, `sklearn`)

2. **Generate synthetic regression data** using:  
   ```python
   make_regression(n_samples=100, n_features=1, n_informative=1)
   ```

3. **Split the data** into training & testing sets using `train_test_split`

4. **Plot the raw data** using a scatter plot

5. **Train a Linear Regression model**  
   - Fit to training data  
   - Print coefficient & intercept  

6. **Train Lasso Regression models** with multiple alpha values:  
   ```
   alpha = [0, 1, 5, 10, 30]
   ```
   For each alpha:
   - Fit Lasso model  
   - Predict values  
   - Plot regression line  

7. **Visualize all models together**  
   - Shows how the line changes as alpha increases  
   - Higher alpha → stronger shrinkage → flatter line  

---

## 📚 Libraries Used

- **NumPy**
- **Pandas**
- **Matplotlib**
- **Scikit-Learn**
  - `make_regression`
  - `train_test_split`
  - `LinearRegression`
  - `Lasso`

---

## 📊 Key Results & Learning

- **α = 0** → same as Linear Regression  
- **Increasing α values** shrink coefficients  
- At high α, the regression line becomes **flatter**  
- L1 regularization (Lasso) can drive coefficients **toward zero**  
- Demonstrates how Lasso controls overfitting using regularization strength  

---

## 🎯 Conclusion

This project provides an intuitive visualization of how **Lasso Regression** behaves with different regularization strengths.  
It helps understand:

- L1 penalty  
- Coefficient shrinkage  
- Effect of α on model flexibility  
- Difference between linear regression and regularized models  
