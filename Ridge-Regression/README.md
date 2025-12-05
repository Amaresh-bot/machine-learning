# 📘 Ridge Regression using Linear Algebra (L2 Regularization)

This project implements **Ridge Regression from scratch** using Python and NumPy, and compares it with **Scikit-Learn’s Ridge model** on the **Diabetes Dataset**.

Ridge Regression improves regular linear regression by adding **L2 regularization**, which helps reduce overfitting and handles multicollinearity. This project focuses on the **core mathematics**, **regularized normal equation**, and **manual implementation** without depending on scikit-learn for the algorithm itself.

---

## ✅ Project Overview

This notebook demonstrates:

- Ridge Regression objective and mathematics  
- Solving coefficients using **regularized normal equations**  
- A custom `MRidge` class implemented using **NumPy**  
- Training/testing using the Diabetes dataset  
- Comparison with Scikit-Learn’s built-in `Ridge` model  
- Evaluation using **R² score**, coefficients, and intercept  

This helps in understanding how Ridge Regression works internally.

---

## 📝 Concept Summary

### 🔷 What is Ridge Regression?

Ridge Regression is a type of **linear regression** that includes **L2 regularization** to reduce overfitting.

The prediction model remains linear:

\[
\hat{Y} = b_0 + b_1 X_1 + b_2 X_2 + \dots + b_n X_n
\]

But the loss function changes to:

\[
J(w) = \|y - Xw\|^2 + \alpha \|w\|^2
\]

Where:

- X: input features  
- y: output target  
- w: model coefficients  
- α: regularization strength  

---

## 🔷 Why Regularization?

Ridge Regression helps when:

- Features are **correlated**  
- Model is **overfitting**  
- Dataset has **many variables**  
- Coefficients are **unstable**  

By adding an L2 penalty, Ridge Regression stabilizes the solution and improves generalization.

---

## 🔷 Matrix Formulation

Ridge Regression uses a modified version of the normal equation:

\[
w = (X^T X + \alpha I)^{-1} X^T y
\]

Where:

- I = Identity matrix  
- αI = Regularization term  

This prevents the matrix from becoming singular and reduces overfitting.

---

## 🔷 Ridge vs Ordinary Linear Regression

| Property | OLS Regression | Ridge Regression |
|---------|----------------|-----------------|
| Loss Function | ‖y - Xw‖² | ‖y - Xw‖² + α‖w‖² |
| Overfitting | More likely | Less likely |
| Coefficients | Can be large | Shrunk toward zero |
| Multicollinearity | Problematic | Handled better |
| Hyperparameter | None | α (regularization strength) |

---

## 💻 Implementation Details

### ✔ Dataset
- Built-in Diabetes dataset from `sklearn.datasets.load_diabetes`

### ✔ Using Scikit-Learn (Benchmark)
```
from sklearn.linear_model import Ridge

reg = Ridge(alpha=0.1)
reg.fit(X_train, y_train)
```

### ✔ Custom Ridge Class (From Scratch)
```
class MRidge:
    def __init__(self, alpha=0.1):
        self.alpha = alpha

    def fit(self, X_train, y_train):
        # Regularized normal equation
        # (X^T X + αI)^−1 X^T y
        ...

    def predict(self, X_test):
        ...
```

### ✔ Evaluation
- R² Score  
- Coefficients  
- Intercept  

---

## 🚀 Technologies Used

- Python  
- NumPy  
- Scikit-Learn  
- Linear Algebra Concepts  
- Google Colab / Jupyter Notebook  

---

## 🎯 Conclusion

This project demonstrates how Ridge Regression works **under the hood**, showing how the regularized normal equation stabilizes coefficients and reduces overfitting. Implementing Ridge Regression manually helps build a strong understanding of:

- L2 regularization  
- Linear algebra in machine learning  
- How ML frameworks compute solutions  

This complements your Multiple Linear Regression project and deepens your core ML fundamentals.
